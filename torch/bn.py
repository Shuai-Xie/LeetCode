import torch
import torch.nn as nn
from torch.nn import Parameter, Module


class BatchNorm(Module):

    def __init__(self, num_features, momentum=0.1, eps=1e-5,
                 affine=True, track_running_stats=True):
        """
        :param num_features: BN dim
        :param momentum: 滑动平均动量
        :param affine: 白化后的 特征放缩
        :param track_running_stats: 训练时统计 batch 内 mean/sigma
        """
        super().__init__()
        self.num_features = num_features
        self.momentum = momentum
        self.eps = eps
        self.affine = affine
        self.track_running_stats = track_running_stats

        # learnable w/b, scale-and-shift
        if self.affine:
            # 将需要 optimize 的 tensor 用 Parameter 表示;
            # 这些会在 model.parameters() 中被加入 optimizer 的优化 params 清单中
            self.weight = Parameter(torch.Tensor(num_features))
            self.bias = Parameter(torch.Tensor(num_features))
        else:
            # register_parameter: The parameter can be accessed as an attribute using given name.
            # 这些虽然 register 作为 module 的 attribute，但不会被加入 model.parameters()
            self.register_parameter('weight', None)  # 注册 attribute, 而 Parameter 定义
            self.register_parameter('bias', None)

        if self.track_running_stats:
            self.register_buffer('running_mean', torch.zeros(num_features))  # mean
            self.register_buffer('running_var', torch.ones(num_features))
            self.register_buffer('num_batches_tracked', torch.tensor(0, dtype=torch.long))
        else:
            self.register_parameter('running_mean', None)
            self.register_parameter('running_var', None)
            self.register_parameter('num_batches_tracked', None)

    def _unsqueeze(self, x):
        return x.unsqueeze(0).unsqueeze(-1)  # 和 input dim 一样

    def forward(self, input: torch.Tensor):
        input_shape = input.size()  # B,C,...
        input = input.view(input.size(0), self.num_features, -1)  # B,C,-1, reshape 成1D

        # normalize / stats
        mean = input.mean([0, 2])
        var = ((input - self._unsqueeze(mean)) ** 2).mean([0, 2])
        inv_std = (var + self.eps) ** (-0.5)  # 更新用的 inv_std，而不是 var
        # std = input.std([0, 2], unbiased=True).clamp(1e-7)

        x_mean = input - self._unsqueeze(mean)
        x_norm = x_mean * self._unsqueeze(inv_std)
        # 保存为反向传播
        self.cache = [x_mean, x_norm, var, inv_std]

        # 更新 buffer
        if self.train():
            self.running_mean = (1 - self.momentum) * self.running_mean + self.momentum * mean
            self.running_var = (1 - self.momentum) * self.running_var + self.momentum * var
            self.num_batches_tracked += 1

        # scale-and-shift
        output = x_norm
        if self.affine:
            output = x_norm * self._unsqueeze(self.weight) + self._unsqueeze(self.bias)

        return output.view(input_shape)

    def backward(self, grad_output):
        """
        https://kratzert.github.io/2016/02/12/understanding-the-gradient-flow-through-the-batch-normalization-layer.html
        """
        x_mean, x_norm, var, inv_std = self.cache

        # 矩阵对向量求导，其他维度 [0,2] 求和
        grad_w = (grad_output * self.x_).sum([0, 2])
        grad_b = (grad_output * 1).sum([0, 2])

        # 白化结果的导数，还要向前求出 转化前 input 的导数
        grad_x_norm = grad_output * self._unsqueeze(self.weight)

        N = x_norm.size(0) * x_norm.size(2)  # 求均值的 N
        grad_mean = 1 / N  # 每一维求和 均值
        grad_var = 1 / N * 2 * x_mean * (1 - grad_mean)
        grad_inv_std = -0.5 * (var + self.eps) ** (-1.5) * grad_var

        grad_input = grad_x_norm * self._unsqueeze(grad_inv_std * x_mean + inv_std * (1 - grad_mean))

        return grad_input, grad_w, grad_b


def demo_modules():
    a = nn.Sequential(  # 外层空
        BatchNorm(10),  # 0
        nn.Sequential(  # 1
            BatchNorm(10, affine=False),  # 1.0
            BatchNorm(10),  # 1.1
        )
    )
    # for k, v in a.named_modules(): # 同层递增标号，深层标号位数+1，如 1.0
    #     print(k)
    #     print(v)

    for k, v in a.named_parameters():  # param_name = moduel_name.param, 如 1.0.weight, 1.0.bias
        print(k)
        print(v)

    # for k, v in a.named_buffers():  # 通过 register 获取到
    #     print(k)
    #     print(v)


def demo_sum():
    a = torch.tensor([[
        [1, 1, 1],
        [2, 2, 2],
        [3, 3, 3],
    ]]).float()  # 1,3,3

    sum_size = a.size(0) * a.size(-1)
    input_sum = a.sum([0, 2])
    input_ssum = (a ** 2).sum([0, 2])

    mean = input_sum / sum_size  # C
    var = input_ssum / sum_size - mean ** 2  # 1/n(a^2) - mean^2
    print(mean, var)

    print(a.mean([0, 2]))
    print(a.var([0, 2]))


demo_sum()
