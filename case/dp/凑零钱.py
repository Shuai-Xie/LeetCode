"""
存在最优子结构，amount 从比 amount 小的面值 逐步增加
子问题之间相互独立，不会出现零和博弈
"""


class Solution:
    # 返回需要的 最少硬币 个数
    # 每种硬币可用 无限次, 就是完全背包问题
    # 但因为 求得不是最终 没用二分法
    def coin_change(self, coins, amount):
        dp = [0] + [amount + 1] * amount
        coins = [0] + coins
        # 遍历硬币面值
        for i in range(1, len(coins)):
            # 总面值
            for j in range(coins[i], amount + 1):  # 完全背包
                dp[j] = min(dp[j], dp[j - coins[i]] + 1)  # 内循环 j 变化时，外循环 i 没变，暗含了 coins[i] 可以选多次
        return dp[-1]

    # 输出所有符合的方案，不要求 coin 个数最少
    def coin_solutions(self, coins, amount):
        coins = [0] + coins
        dp = [[] for _ in range(amount + 1)]
        # for c in coins:  # 单个 coin 的初始状态 不能赋值 这里要表示 i=0 即无商品的状态
        #     dp[c] = [[c]]

        # 方案从 面值=0 的方案 开始转移
        for i in range(1, len(coins)):
            for j in range(coins[i], amount + 1):  # 已经暗含 coins[i] 数量任意
                dp[j] += [li + [coins[i]] for li in dp[j - coins[i]]]
                if not dp[j - coins[i]] and coins[i] == j:  # 添加单个硬币的方案
                    dp[j].append([coins[i]])

        # for i in range(1, amount + 1):
        #     print(i, dp[i])
        return dp[-1]

    def coin_change_recur(self, coins, amount):
        memo = {}  #

        def dfs(n):
            if n in memo:  # 保存中间结果
                return memo[n]
            if n == 0:
                return 0
            if n < 0:  # 无解情况考虑
                return -1

            res = amount + 1  # 不会超过这个数量
            for c in coins:
                sub = dfs(n - c)  # 子问题的数量
                if sub == -1:  # 跳过无解情况
                    continue
                res = min(res, sub + 1)  # update

            memo[n] = res if res < amount + 1 else -1
            return memo[n]

        dfs(amount)
        return memo[amount]


if __name__ == '__main__':
    k = 10
    coins = [2, 3, 5]
    amounts = [8, 13, 18]

    s = Solution()

    for amount in amounts:
        print(amount)
        print(s.coin_change(coins, amount), s.coin_change_recur(coins, amount))
        print(s.coin_solutions(coins, amount))
        exit(0)
