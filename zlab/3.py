"""
DFS 求图像的连通分量
针对给定的图片，写一个算法找出其中非连通的独立白色区域的个数。
注意，只有当两个区域没有任何点相连时才是独立区域。其中，图片1有2个联通区域，图片2有16个联通区域。测试时请使用给定的图片。

leetcode 类似题目 https://leetcode-cn.com/problems/number-of-islands/
"""
import numpy as np

a = np.zeros((10, 10), dtype=int)
a[:2, :2] = 1
a[5:8, 5:8] = 1
a[4][4] = 1


# img: 假设 m x n 矩阵, 0,1 矩阵; 假设 1 为前景
def connect_component(img):
    """
    使用 set 存储所有 前景点的方式，比较占用内存，且计算 set 减法耗时
    """
    h, w = img.shape

    total_pts = []
    for i in range(h):
        for j in range(w):
            if img[i][j] == 1:
                total_pts.append((i, j))

    cnt = 0

    visited = np.zeros_like(img).astype(int)

    while total_pts:
        visited = set()

        # 假设 i,j 为指定以 value=1 的前景 点
        def dfs(i, j):
            if 0 <= i <= h - 1 and 0 <= j <= w - 1 and img[i][j] == 1 and (i, j) not in visited:
                visited.add((i, j))
            else:
                return
            # 4 连通分量
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)

        i, j = total_pts[0]
        dfs(i, j)

        cnt += 1
        total_pts = list(set(total_pts) - visited)

    return cnt




def ccp(img):
    """
    使用 visited 二维数组 记录下访问过的位置
    """
    h, w = img.shape
    visited = np.zeros_like(img).astype(int)

    def dfs(i, j):
        if 0 <= i <= h - 1 and 0 <= j <= w - 1 and img[i][j] == 1 and not visited[i][j]:
            visited[i][j] = 1
            # 4 连通分量
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)

    res = []
    for i in range(h):
        for j in range(w):
            if img[i][j] == 1 and not visited[i][j]:
                # visited[i][j] = 1  # 先记下当前位
                dfs(i, j)
                res.append((j, i))
    print(len(res))
    return res


from PIL import Image
import matplotlib.pyplot as plt

# image 并不是规则的 四边形 连通区域

# note: resize 尺寸太小可能会改变 连通分量的个数，比如比较接近的
a = (np.array(Image.open('a.png').resize((100, 50)).convert('L')) / 255).astype(int)
res = ccp(a)
# res = bingchaji(a)

plt.imshow(a, cmap='gray')

res = np.array(list(res))
plt.scatter(res[:, 0], res[:, 1], s=20, c='r', marker='o')
for i, p in enumerate(res):
    plt.annotate(f'{i + 1}',
                 xy=p, xycoords='data', xytext=(15, -5), textcoords='offset points',
                 color='r', fontsize=10)

plt.show()

# print(connect_component(a))
# print(ccp(a))
