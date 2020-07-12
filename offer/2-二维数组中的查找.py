"""
https://leetcode-cn.com/problems/er-wei-shu-zu-zhong-de-cha-zhao-lcof/
"""
from typing import List

# n*m 二维数组
# 每一行都按照从左到右递增的顺序排序
# 每一列都按照从上到下递增的顺序排序


"""
错误解: 二维二分查找，留下的不是左上方块，而是 mid 左侧矩形 或 上侧矩形
"""


class Solution:

    # 思考不够透彻的 递归查找，耗时，不是最好的解决方案
    def findNumberIn2DArray_naive(self, matrix: List[List[int]], target: int) -> bool:
        # 问题解：可能数据已经迭代完了，还多余去看了剩下的值
        def findNumberInSubArray(matrix, target):
            if len(matrix) > 0 and len(matrix[0]) > 0:  # 存在数组
                n, m = len(matrix), len(matrix[0])  # n 行, m 列
                lt_i, lt_j, rb_i, rb_j = 0, 0, n - 1, m - 1

                # 判断中间值
                mid_i, mid_j = (lt_i + rb_i) // 2, (lt_j + rb_j) // 2
                mid = matrix[mid_i][mid_j]

                if mid == target:
                    return True
                else:
                    if lt_i == rb_i and lt_j == rb_j:  # 已经是矩阵最后1个数
                        return False  # 全部找完都没有，return False

                    # 分 l, t, r, b 四个矩阵查找
                    if mid > target:  # 左，上
                        l_matrix = [l[:mid_j] for l in matrix]  # 左
                        if findNumberInSubArray(l_matrix, target):
                            return True
                        t_matrix = matrix[:mid_i]  # 上
                        if findNumberInSubArray(t_matrix, target):
                            return True
                    else:  # 右，下
                        r_matrix = [l[mid_j + 1:] for l in matrix]  # 右
                        if findNumberInSubArray(r_matrix, target):
                            return True
                        b_matrix = matrix[mid_i + 1:]  # 下
                        if findNumberInSubArray(b_matrix, target):
                            return True

            return False

        return findNumberInSubArray(matrix, target)

    # 循环
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        # 从右上角开始查找，利用偏序关系 O(m+n) 曼哈顿距离，最多走 m+n
        if len(matrix) > 0 and len(matrix[0]) > 0:  # 要限界，不然报错
            n, m = len(matrix), len(matrix[0])
            i, j = 0, m - 1

            while i < n and j >= 0:
                # 比较 每一行最大的数
                if matrix[i][j] == target:
                    return True
                elif matrix[i][j] < target:  # 去往下一行
                    i += 1
                else:  # 去往左一列
                    j -= 1
        return False

    # 递归 binary search tree
    # 在右上角看就是 二叉查找树
    # l_child(行-1) < node < r_child(列+1)
    def findNumberIn2DArray2(self, matrix: List[List[int]], target: int) -> bool:

        def searchBST(i, j):  # i,j 刻画二叉树节点位置
            if i < n and j >= 0:  # i 做加法，j 减法
                if matrix[i][j] == target:
                    return True
                elif matrix[i][j] < target:  # 右子树，下一行
                    return searchBST(i + 1, j)  # 已经限定在此范围了，所以直接 return
                else:  # 左子树，左一列
                    return searchBST(i, j - 1)
            else:
                return False

        if len(matrix) > 0 and len(matrix[0]) > 0:
            n, m = len(matrix), len(matrix[0])
            return searchBST(0, m - 1)  # 从右上角开始

        return False


a = [
    [1, 4, 7, 11, 15],
    [2, 5, 8, 12, 19],
    [3, 6, 9, 16, 22],
    [10, 13, 14, 17, 24],
    [18, 21, 23, 26, 30]
]
s = Solution()

print(s.findNumberIn2DArray_naive(a, 5))
print(s.findNumberIn2DArray_naive(a, 100))
