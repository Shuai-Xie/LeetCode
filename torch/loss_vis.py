import numpy as np
import matplotlib.pyplot as plt


def focal_loss():
    """
    段长相同情况下，vis 不同 n 取极大值的位置
    乘积: x ** (n / x)
    """

    xs = np.arange(1, 100) / 100

    # 可见 当 p -> 1 时，loss 趋近 0，确信的样本 更少的 loss
    for r in [0, 0.5, 1, 2, 5]:  # r=0 就是 CE LOSS
        ys = [-(1 - x) ** r * np.log(x) for x in xs]
        plt.plot(xs, ys, label=f'r={r}')

    plt.legend()
    plt.title(r'focal loss')
    plt.show()


if __name__ == '__main__':
    focal_loss()
