"""
https://leetcode-cn.com/problems/coin-change-2/

给定不同面额的硬币和一个总金额。每一种面额的硬币有无限个
    写出函数来计算可以凑成总金额的硬币组合数。假设每一种面额的硬币有无限个。
    能组成 面额的 方案
"""
from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        """
        dp[i][j]: 前 i 个硬币，组成 j 的方案
            当前硬币价值 coins[i]
        """
        n = len(coins)
        dp = [[0] * (amount + 1) for _ in range(n + 1)]
        for i in range(n + 1):  # 使用 i 种硬币 组成 0 的方案数
            dp[i][0] = 1

        for i in range(1, n + 1):  # 硬币
            for j in range(1, amount + 1):
                if j >= coins[i - 1]:  # 能放下时
                    dp[i][j] = dp[i - 1][j] + dp[i][j - coins[i - 1]]  # 不用 + 用
                else:  # 不能放下当前硬币时
                    dp[i][j] = dp[i - 1][j]  # 继承 i-1 种硬币的方案数
        return dp[-1][-1]

    def change2(self, amount: int, coins: List[int]) -> int:
        """
        完全背包，每个硬币可用无限个，能组成面额 amount 的组合
        """
        dp = [0] * (amount + 1)
        dp[0] = 1
        n = len(coins)

        # 只有 i-1 时刻有关 优化
        for i in range(1, n + 1):
            for j in range(1, amount + 1):
                if j >= coins[i - 1]:
                    dp[j] = dp[j] + dp[j - coins[i - 1]]  # 后者 < j，在之前已更新到 使用 i 商品后的方案数
        return dp[-1]
