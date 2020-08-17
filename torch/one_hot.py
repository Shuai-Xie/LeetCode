"""
https://blog.csdn.net/qq_34914551/article/details/88700334

tensor.scatter_(dim, index, src)
    dim     指定了覆盖数据是从哪个轴作为依据。后面再详细解释。值的范围是从0到 sum(tensor.shape)-1
    index   告诉函数要将 src 中对应的值放到 tensor 的哪个位置。index 的 shape 要和 src 一致，或者 src 可以通过广播机制实现 shape 一致。
    src     保存了想用来覆盖 tensor的值
"""
import torch
import numpy as np
import torch.sparse


def demo_scatter():
    x = torch.rand(2, 5)
    print(x)

    index = torch.from_numpy(np.array([
        [0, 1, 2, 0, 0],
        [2, 0, 0, 1, 2]
    ])).long()

    # index 和 x 的 shape 一致
    # 使用 x 来覆盖 b

    # dim=0, 即 index 中指定的数值为 行号;
    # 而 index 整个值所在的位置; 对应在 b 中位置的 剩下维度

    # 10个位置 -> 从 x 到 b 的元素映射位置
    # [0,0], [1,1], [2,2], [0,3], [0,4]
    # [2,2], [0,1], [0,2], [1,3], [2,4]
    b = torch.zeros(3, 5).scatter_(0, index, x)
    print(b)


batch_size = 3
class_num = 5


def fc_one_hot1():  # scatter_
    """scatter_
    dim: 指定 tensor 中那一维 用 index
    原理: 将 label 作为 index
        label value -> dim=1 列号
        label pos   -> 原始 label 的行号, batch idx
    """
    label = torch.randint(class_num, (batch_size, 1))  # (3,1)
    print(label)
    y_one_hot = torch.zeros(batch_size, class_num).scatter_(1, label, 1)  # (3,10)
    print(y_one_hot)


def fc_one_hot2():
    """index_select
    dim: 指定 tensor 维度
    """
    label = torch.randint(class_num, (batch_size,))  # (3,)
    print(label)
    ones = torch.sparse.torch.eye(class_num)  # eye 矩阵
    y_one_hot = ones.index_select(0, label)  # label 作为剩下维度指定
    print(y_one_hot)


def seg_one_hot1():
    """
    将 B,H,W 的 label 先转成 1D element-wise
    再用 index_select, 最后 view 回原始 size，并 permute

    但是 无法处理包含 bg idx 的 label
    """
    B, H, W = 1, 2, 3
    label = torch.randint(class_num, (B, H, W))
    print(label)

    label = label.view(-1)  # 转成 element-wise 1D
    ones = torch.sparse.torch.eye(class_num)
    y_one_hot = ones.index_select(0, label)  # 会自动扩充
    print(y_one_hot)

    # resize 到原始尺寸
    y_one_hot = y_one_hot.view(B, H, W, class_num)  # 类别 C 体现在最后一维
    print(y_one_hot)
    print(torch.argmax(y_one_hot, dim=-1))

    return y_one_hot.permute(0, 3, 1, 2)


def seg_one_hot2():
    """
    将 B,H,W 的 label 先转成 1D element-wise
    再用 index_select, 最后 view 回原始 size，并 permute

    但是 无法处理包含 bg idx 的 label
    """
    B, H, W = 1, 2, 3
    bg_idx = 255
    label = torch.randint(class_num, (B, H, W))
    print(label)
    label[0][0][0] = bg_idx

    y = torch.zeros(class_num, B, H, W)
    for i in range(class_num):
        y[i][label == i] = 1
    print(y.permute(1, 2, 3, 0))  # 让 class 维在最后; 因为000=bg，所以没有

    y = y.permute(1, 0, 2, 3)
    print(torch.argmax(y, dim=1))

    return y


# fc_one_hot1()
# fc_one_hot2()
# seg_one_hot1()
seg_one_hot2()
