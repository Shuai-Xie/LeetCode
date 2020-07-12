import matplotlib.pyplot as plt
import numpy as np


def plt_lr_schedulers():
    num_epochs = 200  # epoch 越大，最后的 lr 越小
    lr = 0.1

    epochs = np.arange(num_epochs)

    poly_lr = lr * (1 - epochs / num_epochs) ** 0.9
    cos_lr = 0.5 * lr * (1 + np.cos(epochs / num_epochs * np.pi))

    plt.figure()
    plt.plot(epochs, poly_lr, '-', label='poly')  # 添加 label 会显示在图例中
    plt.plot(epochs, cos_lr, 'g-', label='cos')
    plt.yticks(np.arange(0, 0.11, 0.01))

    plt.legend(loc='upper right')
    plt.xlabel('epochs')
    plt.ylabel('learning rate')

    plt.show()


if __name__ == '__main__':
    plt_lr_schedulers()
