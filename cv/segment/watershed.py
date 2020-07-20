"""
https://zhuanlan.zhihu.com/p/67741538
图像语义分割 分水岭算法, opencv 基于 marker 改进
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('coin.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 双峰图，OSTU 二值化
ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)  # 162, 会返回自适应选取的阈值

# noise removal
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))  # 方形结构元
# 开操作; 断开细小的连接位置；并去除背景噪点
opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=2)


def subplots(imgs, titles):
    num = len(imgs)
    f, ax = plt.subplots(1, num, figsize=(num * 2, 3), dpi=150)
    for idx, im in enumerate(imgs):
        ax[idx].imshow(im, cmap='gray')  # 1行 [0,idx] 报错
        ax[idx].set_title(titles[idx])
        ax[idx].axis('off')
    plt.show()


def morph_op():
    # 膨胀
    sure_bg = cv2.dilate(opening, kernel, iterations=2)  # sure background area
    # 腐蚀
    sure_fg = cv2.erode(opening, kernel, iterations=2)  # sure foreground area
    # 减法  膨胀-腐蚀 = 图像的边缘
    # unknown area 剩下的区域不确定是硬币还是背景
    # 这些区域通常在前景和背景接触的区域(或者两个不同硬币接触的区域)，我们称之为边界
    # 通过分水岭算法应该能找到确定的边界
    unknown = cv2.subtract(sure_bg, sure_fg)

    subplots([thresh, opening, sure_bg, sure_fg, unknown],
             ['thresh', 'opening', 'sure_bg', 'sure_fg', 'unknown'])


def dist_trans_op():  # 比 morph_op 更好提取出前景
    # 距离转换图像，其中每个像素的值为其到最近的背景像素（灰度值为0）的距离，
    # 可以看到硬币的中心像素值最大（中心离背景像素最远）。
    # 对其进行二值处理就得到了分离的前景图，白色区域肯定是硬币区域，而且还相互分离
    dist_trans = cv2.distanceTransform(opening, distanceType=cv2.DIST_L2, maskSize=5)
    # print(np.unique(opening))  # {0,255}
    # print(np.unique(dist_trans))  # [0, max_D], 1 与最近的 0 的距离

    # 正则化
    cv2.normalize(dist_trans, dist_trans, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX)
    # print(np.min(dist_trans), np.max(dist_trans))  # [0,1]

    # max_val/2 二值化
    ret, sure_fg = cv2.threshold(dist_trans, thresh=0.5 * dist_trans.max(), maxval=255, type=cv2.THRESH_BINARY)
    # print(np.min(sure_fg), np.max(sure_fg))  # [0,255.0]

    sure_fg = sure_fg.astype('uint8')

    # Mask size should be 3 or 5 or 0 (precise), 越大越稀疏
    # subplots([opening, dist_trans, sure_fg],
    #          ['opening', 'dist_trans', 'sure_fg'])

    # 膨胀
    sure_bg = cv2.dilate(opening, kernel, iterations=2)  # sure background area

    # 返回边界区域
    unknown = cv2.subtract(sure_bg, sure_fg)
    return sure_fg, unknown


sure_fg, unknown = dist_trans_op()

ret, markers = cv2.connectedComponents(sure_fg)
# print(np.unique(markers))  # 连通分量图, 从 0; 1-24

markers += 1  # 求完 fg 得到的 bg 设置为 1 -> 1; 2-25

# Now, mark the region of unknown with zero
markers[unknown == 255] = 0
# [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25]
# 定义背景 和 连通分量
# 1 作为 sure_bg，一大块连通分量
# 0 unknown 区域，watershed 算法从这里开始 flooding
# markers: seeds of the future image regions;
# 粗略表示的 fg 连通分量，由 watershed 找到精确边界

# 使用分水岭算法执行基于标记的图像分割，将图像中的对象与背景分离
markers = cv2.watershed(img, markers)
print(np.unique(markers))
# [-1  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25]

img[markers == -1] = [0, 0, 255]  # 将边界标记为红色

plt.imshow(img[:, :, ::-1])
plt.show()

# markers_copy = markers.copy()
# markers_copy[markers == 0] = 150  # 灰色表示背景, unknown bg
# markers_copy[markers == 1] = 0  # 黑色表示背景,
# markers_copy[markers > 1] = 255  # 白色表示前景
# markers_copy = np.uint8(markers_copy)
#
# subplots([sure_fg, unknown, markers, markers_copy],
#          ['sure_fg', 'unknown', 'markers', 'markers_copy'])
