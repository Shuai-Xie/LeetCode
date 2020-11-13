"""
https://leetcode-cn.com/problems/n-queens/
"""
from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        """
        返回所有不同的 n 皇后问题的解决方案
        皇后彼此不能相互攻击，也就是说：任何两个皇后都不能处于同一条横行、纵行或斜线上。
        """
        res = []
        path = []

        def is_valid_column(cur_row, cur_col):  # 判断之前 r-1 行是否满足
            if cur_row == 0:  # 当前第0行，肯定随便选位置
                return True

            # 当前行 r; 同行没有，左下，右下 也没有; 只用判断 左上，正上，右上

            # 前面行
            for row in range(cur_row - 1, -1, -1):
                if path[row][cur_col] == 'Q':
                    return False
                gap = cur_row - row
                left_col = cur_col - gap
                if left_col >= 0 and path[row][left_col] == 'Q':
                    return False
                right_col = cur_col + gap
                if right_col < n and path[row][right_col] == 'Q':
                    return False
            return True

        def get_line(col):  # Q 所在行号
            return '.' * col + 'Q' + '.' * (n - col - 1)

        def dfs(r):  # 当前所在行号
            nonlocal path
            if r == n:
                res.append(path[:])  # 一定要这样
                return

            # 列号
            for i in range(n):
                # 结合之前 r-1 行做出的选择，判断当前 r 行可选哪些列
                if is_valid_column(r, i):
                    # 当前行选择
                    line = get_line(i)
                    path.append(line)
                    # 去往下一行
                    dfs(r + 1)
                    path.pop()  # 去掉尾部元素

        dfs(0)
        return res


s = Solution()
n = 4
print(s.solveNQueens(n))
