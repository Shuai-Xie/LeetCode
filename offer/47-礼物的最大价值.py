"""
在一个 m*n 的棋盘的每一格都放有一个礼物，每个礼物都有一定的价值（价值大于 0）。
你可以从棋盘的左上角开始拿格子里的礼物，并每次向右或者向下移动一格、直到到达棋盘的右下角。
给定一个棋盘及其上面的礼物的价值，请计算你最多能拿到多少价值的礼物？

链接：https://leetcode-cn.com/problems/li-wu-de-zui-da-jie-zhi-lcof
"""

from typing import List


class Solution:
    def maxValue(self, grid: List[List[int]]) -> int:
        # grid.len > 0, grid[0].len > 0
        m, n = len(grid), len(grid[0])
        dp = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    dp[i][j] = grid[i][j]
                elif i == 0:  # 只能从左边来
                    dp[i][j] = dp[i][j - 1] + grid[i][j]
                elif j == 0:  # 只能从上部来
                    dp[i][j] = dp[i - 1][j] + grid[i][j]
                else:  # 可左，可上
                    dp[i][j] = max(dp[i][j - 1] + grid[i][j], dp[i - 1][j] + grid[i][j])
        return dp[m - 1][n - 1]

    def maxValue2(self, grid: List[List[int]]) -> int:
        # 不分配额外空间
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i == 0 and j == 0:
                    continue
                elif i == 0:  # 只能从左边来
                    grid[i][j] += grid[i][j - 1]
                elif j == 0:  # 只能从上部来
                    grid[i][j] += grid[i - 1][j]
                else:  # 可左，可上
                    grid[i][j] = max(grid[i][j - 1] + grid[i][j], grid[i - 1][j] + grid[i][j])
        return grid[-1][-1]


grids = [
    [1, 3, 1],
    [1, 5, 1],
    [4, 2, 1]
]

s = Solution()
print(s.maxValue(grids))
