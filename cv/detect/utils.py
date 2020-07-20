import numpy as np
import matplotlib.pyplot as plt


def plt_dets(dets):
    side = int(np.max(dets[:, 0:4])) + 10
    canvas = np.ones((side, side, 3))  # float 类型

    plt.figure()
    plt.imshow(canvas)
    for box in dets:
        plt.gca().add_patch(
            plt.Rectangle(
                xy=box[:2], width=box[2] - box[0], height=box[3] - box[1],  # box
                # color='yellow',
                fill=False,  # 不填充矩形，必须设置
                edgecolor='green',
                linewidth=2,
            )
        )
        plt.annotate(s=str(box[-1]),
                     xy=box[:2], xycoords='data', xytext=(0, +5), textcoords='offset points',
                     color='k', fontsize=10)
    plt.show()
