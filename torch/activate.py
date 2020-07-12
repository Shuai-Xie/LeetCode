import torch
import torch.nn.functional as F
import matplotlib.pyplot as plt
# python 的可视化模块, 教程 (https://morvanzhou.github.io/tutorials/data-manipulation/plt/)


def plt_activations(x):
    # 几种常用的 激励函数
    y_relu = F.relu(x)
    y_sigmoid = torch.sigmoid(x)
    y_tanh = torch.tanh(x)
    y_softplus = F.softplus(x)  # 在 0 附近缓慢增加，逐渐和 x 接近
    # softplus, 'softtened' version of relu = max(0,x)
    # y = log(1+exp(x))

    plt.figure()

    plt.plot(x.numpy(), y_relu.numpy(), '-', label='relu')
    plt.plot(x.numpy(), y_sigmoid.numpy(), '-', label='sigmoid')
    plt.plot(x.numpy(), y_tanh.numpy(), '-', label='tanh')
    plt.plot(x.numpy(), y_softplus.numpy(), '-', label='softplus')

    plt.ylim([-2, 11])
    plt.legend(loc='best')
    plt.show()


def rsigmoid(x, r):
    return 1 / (1 + r * torch.exp(-x))


def plt_rsigmoid(x, r_vals):
    plt.figure()

    for r in r_vals:
        y = rsigmoid(x, r)
        plt.plot(x.numpy(), y.numpy(), '-', label=f'r={r}')
        # plt.plot(y.numpy(), x.numpy(), '-', label=f'r={r}')

    plt.hlines(y=0.5, xmin=-10, xmax=10, colors='gray', linestyles='-')
    plt.vlines(x=0, ymin=0, ymax=1, colors='gray', linestyles='-')
    plt.legend(loc='best')
    plt.show()


if __name__ == '__main__':
    x = torch.linspace(-10, 10, 100)
    plt_activations(x)

    plt_rsigmoid(x, r_vals=[0.1, 1, 100])
