import numpy as np


def _whctrs(anchor):
    """
    Return width, height, x center, and y center for an anchor (window).
    """
    w = anchor[2] - anchor[0] + 1
    h = anchor[3] - anchor[1] + 1
    x_ctr = anchor[0] + 0.5 * (w - 1)
    y_ctr = anchor[1] + 0.5 * (h - 1)
    return w, h, x_ctr, y_ctr


def _mkanchors(ws, hs, x_ctr, y_ctr):
    """
    Given a vector of widths (ws) and heights (hs) around a center
    (x_ctr, y_ctr), output a set of anchors (windows).
    """
    ws = ws[:, np.newaxis]
    hs = hs[:, np.newaxis]
    anchors = np.hstack((x_ctr - 0.5 * (ws - 1),
                         y_ctr - 0.5 * (hs - 1),
                         x_ctr + 0.5 * (ws - 1),
                         y_ctr + 0.5 * (hs - 1)))
    return anchors


def _ratio_enum(anchor, ratios):
    """
    Enumerate a set of anchors for each aspect ratio wrt an anchor.
    Args:
        anchor: [0,0,15,15]
        ratios: (0.5, 1, 2) 面积比例

    Returns:
        base_anchor 下 ratios (0.5, 1, 2) 对应的 3 种 anchor 边界 x1,y1,x2,y2
    """
    w, h, x_ctr, y_ctr = _whctrs(anchor)  # 16 16 7.5 7.5
    size = w * h  # 256
    size_ratios = size / ratios  # 面积比例; * 变成 list 扩充了
    ws = np.round(np.sqrt(size_ratios))
    hs = np.round(ws * ratios)
    anchors = _mkanchors(ws, hs, x_ctr, y_ctr)
    return anchors


def _scale_enum(anchor, scales):
    """
    Enumerate a set of anchors for each scale wrt an anchor.
    将 anchor w,h 使用 scales 放缩得到 3 组
    """

    w, h, x_ctr, y_ctr = _whctrs(anchor)
    ws = w * scales
    hs = h * scales
    anchors = _mkanchors(ws, hs, x_ctr, y_ctr)
    return anchors


def generate_anchors(base_size=16, ratios=(0.5, 1, 2),
                     scales=2 ** np.arange(3, 6)):
    """
    Generate anchor (reference) windows by enumerating aspect ratios X
    scales wrt a reference (0, 0, 15, 15) window.
    Args:
        base_size: 16
        ratios: box 三种比例 0.5,1,2 生成 size 下的对应 长宽比
        scales: 2 ** np.arange(3, 6) 放缩 box 大小
    """

    base_anchor = np.array([1, 1, base_size, base_size]) - 1  # 1,1,16,16; 基础大小，左上右下
    ratio_anchors = _ratio_enum(base_anchor, ratios)  # 3,4
    anchors = np.vstack([_scale_enum(ratio_anchors[i, :], scales)
                         for i in range(ratio_anchors.shape[0])])
    return anchors


if __name__ == '__main__':
    anchors = generate_anchors()
    print(anchors)
