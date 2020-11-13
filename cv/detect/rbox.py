from shapely.geometry import Polygon
import numpy as np
import cv2
import matplotlib.pyplot as plt


def intersection(gt, pred):
    gt = np.asarray(gt)
    pred = np.asarray(pred)
    gt = Polygon(gt[:8].reshape((4, 2)))  # 4,2
    pred = Polygon(pred[:8].reshape((4, 2)))
    if not gt.is_valid or not pred.is_valid:
        return 0
    # 计算倾斜多边形的交集
    inter = Polygon(gt).intersection(Polygon(pred)).area
    union = gt.area + pred.area - inter
    if union == 0:
        return 0
    else:
        return inter / union


def demo_inter():
    canvas = np.zeros((100, 100, 3), dtype=int)

    gt = np.array([[0, 60], [60, 0], [80, 0], [0, 80]], dtype=int)
    pred = np.array([[0, 20], [100, 20], [100, 40], [0, 40]], dtype=int)

    cv2.fillPoly(canvas, [gt], color=(255, 0, 0))
    cv2.fillPoly(canvas, [pred], color=(0, 255, 0))

    inter = Polygon(gt).intersection(Polygon(pred))

    # https://stackoverflow.com/questions/20474549/extract-points-coordinates-from-a-polygon-in-shapely
    x, y = inter.exterior.coords.xy  # 提取 Polygon 对象的 coords
    inter = np.array([x, y], dtype=int).T
    inter = inter[::-1, :]  # 去掉首个点

    cv2.fillPoly(canvas, [inter], color=(255, 255, 0))

    plt.imshow(canvas)
    plt.show()
