import numpy as np
from sklearn.cluster import KMeans
from sklearn_extra.cluster import KMedoids

"""
https://www.cnblogs.com/wenhoujx/p/3147563.html
"""

# 生成一个随机数据，样本大小为100, 特征数为3
data = np.random.rand(10, 3)


# cluster 中心为 计算出来的 mean
def kmeans():
    # 假如我要构造一个聚类数为3的聚类器
    estimator = KMeans(n_clusters=3)  # 构造聚类器
    estimator.fit(data)  # 聚类
    label_pred = estimator.labels_  # 获取聚类标签
    centroids = estimator.cluster_centers_  # 获取聚类中心

    # 聚类中心，平均值计算得到的，c 可能不在 data 中
    print(label_pred)
    print(centroids)
    print(np.argwhere(data == centroids))


# cluster 中心为 真实的数据点
def kmediods():
    estimator = KMedoids(n_clusters=3)
    estimator.fit(data)  # 聚类
    label_pred = estimator.labels_  # 获取聚类标签
    centroids = estimator.cluster_centers_  # 获取聚类中心

    # 聚类中心，平均值计算得到的，c 可能不在 data 中
    print(label_pred)
    print(centroids)
    print(estimator.n_clusters)
    exit(0)

    # 判断 d 在 centroids 的简单方法：if d in centroids

    finds = []
    for idx, d in enumerate(data):  # 要得到 idx，所以不删 data 中出现的元素
        for i, c in enumerate(centroids):
            if (d == c).all():  # all() 元素全相等, any() 存在1个相等即可
                finds.append(idx)
                centroids = np.delete(centroids, i, axis=0)  # 删一行，别跳出删，就删完了
                break
        if len(centroids) == 0:
            break

    print(finds)


if __name__ == '__main__':
    # kmeans()
    # kmediods()

    a = [1, 2, 3, 4, 5]
    a = [str(i) for i in a]
    with open('select.txt', 'w') as f:
        for p in a:
            f.write(p + '\n')
