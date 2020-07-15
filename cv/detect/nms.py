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


def nms_thre(dets, thre):  # iou thre
    x1 = dets[:, 0]
    y1 = dets[:, 1]
    x2 = dets[:, 2]
    y2 = dets[:, 3]
    scores = dets[:, 4]

    # 计算每个 box 的面积，并对 box 按照 score 降序排列
    areas = (x2 - x1 + 1) * (y2 - y1 + 1)  # 边界线也计算了
    order = scores.argsort()[::-1]  # score 从高到低

    keep = []
    while len(order) > 0:
        i = order[0]  # 取出 score 最高者
        keep.append(i)  # 保留簇中得分最高的

        # inter box 坐标计算
        # 不管 其他 box 相对于 box_i 在哪，inter_box 坐标计算方式不变
        xx1 = np.maximum(x1[i], x1[order[1:]])  # 前面已得到 x1, 只要取出，计算 iou box 的 x
        yy1 = np.maximum(y1[i], y1[order[1:]])
        xx2 = np.minimum(x2[i], x2[order[1:]])
        yy2 = np.minimum(y2[i], y2[order[1:]])

        # 相交面积，保证不相交的 = 0
        w = np.maximum(0., xx2 - xx1 + 1)
        h = np.maximum(0., yy2 - yy1 + 1)
        inter = w * h
        union = areas[i] + areas[order[1:]] - inter

        ious = inter / union

        # 除去 i 和 iou>thre 后剩下的 box
        # 注意：ious 的 idx 相交 order 少了 1，因为 ious 中不包括 取出的 order[0]
        remain_inds = np.where(ious <= thre)[0]  # 留下的 box
        order = order[remain_inds + 1]  # 更新 order

    return keep


if __name__ == '__main__':
    dets = np.array([
        [100, 120, 170, 200, 0.98],
        [20, 40, 80, 90, 0.99],
        [20, 38, 82, 88, 0.96],
        [200, 380, 282, 488, 0.9],
        [19, 38, 75, 91, 0.8]
    ])
    plt_dets(dets)

    keep = nms_thre(dets, 0.5)

    dets = dets[keep]
    plt_dets(dets)
