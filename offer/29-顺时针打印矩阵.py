"""
从外向里以顺时针 打印矩阵

输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
输出：[1,2,3,6,9,8,7,4,5]
"""

from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        if len(matrix) > 0 and len(matrix[0]) > 0:
            l, r, t, b = 0, len(matrix[0]) - 1, 0, len(matrix) - 1
            while True:
                for j in range(l, r + 1):
                    res.append(matrix[t][j])  # top, j 索引 column
                t += 1  # 模拟更新上方边界
                if t > b:
                    break

                for i in range(t, b + 1):
                    res.append(matrix[i][r])
                r -= 1  # 右边界 左移
                if l > r:
                    break

                for j in range(r, l - 1, -1):  # 到 l 停止
                    res.append(matrix[b][j])
                b -= 1  # 下边界 上移
                if t > b:
                    break

                for i in range(b, t - 1, -1):
                    res.append(matrix[i][l])
                l += 1  # 左边界 右移
                if l > r:
                    break

        return res
