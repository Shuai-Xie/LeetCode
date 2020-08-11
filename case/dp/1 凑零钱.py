"""
存在最优子结构，amount 从比 amount 小的面值 逐步增加
子问题之间相互独立，不会出现零和博弈
"""


# 递归，自上而下，使用 memo 存储中间结果
def coin_change(coins, amount):
    memo = {}

    def dp(n):
        # 查备忘录
        if n in memo:
            return memo[n]
        # base case
        if n == 0:
            return 0
        if n < 0:
            return -1  # 无解

        # 求最小值，初始化为正无穷
        res = float('inf')
        for coin in coins:
            subproblem = dp(n - coin)  # 自顶向下，最后1个coin可以是任意一个；递归就表明了每个 coin 可用无限次
            if subproblem == -1:
                continue
            res = min(res, 1 + subproblem)
        # 得到 n 最优解，存入 memo
        memo[n] = res if res != float('inf') else -1
        return memo[n]

    return dp(amount)


# dp 自底向上
def coin_change_dp(coins, amount):
    dp = [amount + 1] * (amount + 1)  # dp[n], amount=n 时，最少应用硬币个数
    dp[0] = 0  # amount=0 需要的硬币数量

    for i in range(1, amount + 1):
        for c in coins:  # 内循环 for 表示可用 coin 无限次
            if i - c >= 0:  # 原来 dp[i] 就是还没用当前 c 的状体
                dp[i] = min(dp[i], dp[i - c] + 1)  # 是否要用 coin c
    return dp[-1]


# 保存所有 方案
def coin_change_solutions(coins, amount):
    dp = [amount + 1] * (amount + 1)
    dp[0] = 0  # amount=0 需要的硬币数量
    s = [[] for _ in range(amount + 1)]  # 保存最优结果

    # 逐个 coin 遍历，得到的 solution 是全排列
    for i in range(1, amount + 1):
        for c in coins:
            if i - c >= 0:
                if dp[i - c] + 1 < dp[i]:  # 从 i-c 方案转移
                    dp[i] = dp[i - c] + 1
                    if not s[i - c]:  # s[i-c] 为 [] 情况
                        s[i] = [[c]]
                    else:
                        s[i] = [li + [c] for li in s[i - c]]
                elif dp[i - c] + 1 == dp[i]:
                    if not s[i - c]:
                        s[i] += [[c]]
                    else:
                        s[i] += [li + [c] for li in s[i - c]]

    return s[-1]


if __name__ == '__main__':
    k = 10
    coins = [1, 2, 5]
    amounts = [8, 13, 18]

    for a in amounts:
        print(a)
        # print(coin_change(coins, a), coin_change_dp(coins, a))
        res = coin_change_solutions(coins, a)
        print(res)
        print(len(res))
        print()
