"""
存在最优子结构，amount 从比 amount 小的面值 逐步增加
子问题之间相互独立，不会出现零和博弈
"""


class Solution:
    def coin_change_dp(self, coins, amount):
        """
        :param coins: 可选的面值，无限个，完全背包
        :param amount: 凑零钱总数

        dp[i] 表示最少方案 使用的硬币数量
        """
        n = len(coins)
        dp = [0] + [amount + 1] * amount
        # 面值=0，用0个;
        # 其他面值 由于还未使用硬币，所以初始化 >amount 即可，因为最小面值为 1，不可能超过 amount

        for i in range(n):
            for j in range(coins[i], amount + 1):  # 完全背包，随着 j 增加，coins[i] 使用数量也在累加
                dp[j] = min(dp[j], dp[j - coins[i]] + 1)
        return dp[-1]

    def coin_change_recur(self, coins, amount):
        """
        递归法，自上而下，并将子问题的解存入 memo
        """

        memo = {}  # 记录每个面值的 最少硬币数量

        def dfs(amount):
            if amount in memo:
                return memo[amount]
            if amount == 0:
                return 0
            if amount < 0:  # 无解
                return -1

            res = amount + 1
            for c in coins:
                ans = dfs(amount - c)  # 无解情况 不要更新
                if ans > -1:
                    res = min(res, ans + 1)
            if res == amount + 1:
                res = -1
            memo[amount] = res
            return res

        return dfs(amount)

    def coin_change_solutions(self, coins, amount):
        """
        保存所有可行的方案
        大方案 都是从 子方案 转移来的，在子方案基础上 添加新 coin 即可
        dp[i] 表示 此面值下的 所有方案
        """
        n = len(coins)
        dp = [[] for _ in range(amount + 1)]  # 每个 list 保存由 list 组成的方案

        for i in range(n):
            for j in range(coins[i], amount + 1):
                dp[j] += [li + [coins[i]] for li in dp[j - coins[i]]]  # 注意是 +=
                # 当 dp[j - coins[i]] 为空时，单个硬币组成的方案 无法通过 for 加入；补充
                if not dp[j - coins[i]] and coins[i] == j:
                    dp[j].append([coins[i]])
        print('amount:', amount, 'solutions:', len(dp[-1]))
        print(dp[-1])

    def coin_change_solution_num(self, coins, amount):  # 方案总数
        n = len(coins)
        dp = [0] * (amount + 1)
        dp[0] = 1

        for i in range(n):
            for j in range(coins[i], amount + 1):
                # -coins[i] 后，所有子面值的方案数; 都可以作为 dp[j] 子方案
                dp[j] += dp[j - coins[i]]  # 从面值 0 转移过来也是 方案

        return dp[-1]


W = 10
coins = list(range(1, W + 1))
amount = 4

s = Solution()
s.coin_change_solutions(coins, amount)
