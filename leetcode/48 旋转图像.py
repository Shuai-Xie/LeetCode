"""
给定一个 n × n 的二维矩阵表示一个图像。
将图像顺时针旋转 90 度。
inplace 旋转，不能开辟另一内存

给定 matrix =
[
  [1,2,3],
  [4,5,6],
  [7,8,9]
],

原地旋转输入矩阵，使其变为:
[
  [7,4,1],
  [8,5,2],
  [9,6,3]
]
"""
from typing import List
import numpy as np


class Solution:
    def rotate2(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        先转置，后镜像对称 O(n^2)
        使用了两次矩阵操作，矩阵所有元素都被赋值了2次
        """
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return
        n = len(matrix)

        # 转置 (i,j) -> (j,i)
        for i in range(n):
            for j in range(i, n):  # 反上三角矩阵
                # swap
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        # 横着镜像对称 (i,j) -> (i,n-1-j)
        for i in range(n):
            for j in range(n // 2):  # 奇偶均可
                matrix[i][j], matrix[i][n - 1 - j] = matrix[i][n - 1 - j], matrix[i][j]

        print(np.array(matrix))

    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        先转置，后镜像对称 O(n^2)
        """
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return
        n = len(matrix)

        # 1/4 区域，因为每次变换4个值
        # (i,j) -> (j,n-1-i) 旋转对应关系
        for i in range(n // 2 + n % 2):  # 奇数别忘记旋转中间行，和镜像对称不同
            for j in range(n // 2):
                # 连续值更新时，从尾部赋值更节省IO，因为先赋后面，不改变前面值，只要保存末尾数字即可
                # 如果正序更新，更新后，后面值就取不到原始的前面值了
                tmp = matrix[n - 1 - j][i]
                matrix[n - 1 - j][i] = matrix[n - 1 - i][n - 1 - j]
                matrix[n - 1 - i][n - 1 - j] = matrix[j][n - 1 - i]
                matrix[j][n - 1 - i] = matrix[i][j]
                matrix[i][j] = tmp

                # tmp = []
                # row, col = i, j
                #
                # # store 4 elements in tmp
                # for k in range(4):
                #     tmp.append(matrix[row][col])
                #     row, col = col, n - 1 - row  # 加第4个又回到原点
                # for k in range(4):
                #     matrix[row][col] = tmp[(k - 1) % 4]  # 取模，不用平移元素
                #     row, col = col, n - 1 - row

        print(np.array(matrix))


s = Solution()
m = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
m2 = [
    [5, 1, 9, 11],
    [2, 4, 8, 10],
    [13, 3, 6, 7],
    [15, 14, 12, 16]
]
m3 = [
    [1]
]
print(np.array(m))
s.rotate(m)
print(np.array(m2))
s.rotate(m2)
print(np.array(m3))
s.rotate(m3)
