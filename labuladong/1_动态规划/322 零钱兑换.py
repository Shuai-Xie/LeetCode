"""
https://leetcode-cn.com/problems/coin-change/

给定不同面额的硬币 coins 和一个总金额 amount。
编写一个函数来计算可以凑成总金额所需的 最少的硬币个数。如果没有任何一种硬币组合能组成总金额，返回 -1。

你可以认为每种硬币的数量是无限的。
"""
from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        最小硬币面值是 1，那么初始状体可定义为 amount+1
        """
        # dp[i] 面值为 i 最少需要的硬币数量; 初始化为 amout+1 判断是否发生更新
        dp = [amount + 1] * (amount + 1)
        # base case
        dp[0] = 0

        # for c in coins:  # 可选的硬币
        #     for i in range(c, amount + 1):  # 硬币面值
        #         dp[i] = min(dp[i], dp[i - c] + 1)  # 选择是否使用当前面值

        # 另一种写法; 理解更清楚，每一个 i 都取得最优后，才向后继续获取更大的面值
        for i in range(amount + 1):  # 所有币值
            for c in coins:
                if i < c:
                    continue
                dp[i] = min(dp[i], dp[i - c] + 1)  # 使用当前硬币

        return -1 if dp[-1] == amount + 1 else dp[-1]

    def coinChange2(self, coins: List[int], amount: int) -> int:
        memo = {}  # 存储 每个 amout 的最少硬币数量

        def dfs(am):  # 子 币值
            if am in memo:
                return memo[am]
            if am == 0:
                return 0
            if am < 0:  # 不可解
                return -1

            # 每种硬币 无限使用，所以递归进入仍可遍历每一个
            ans = am + 1
            for c in coins:
                sub_ans = dfs(am - c)
                if sub_ans > -1:
                    ans = min(ans, sub_ans + 1)  # + 当前使用的硬币 c
            # 不存在解，没有更新结果
            if ans == am + 1:
                ans = -1
            memo[am] = ans
            return ans

        return dfs(amount)


s = Solution()
coins = [1, 2, 5]
amount = 11
# coins = [2]
# amount = 3
# coins = [1]
# amount = 0
# coins = [186, 419, 83, 408]
# amount = 6249
print(s.coinChange(coins, amount))
print(s.coinChange2(coins, amount))
