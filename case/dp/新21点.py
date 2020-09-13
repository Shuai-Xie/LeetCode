class Solution:
    def new21Game(self, N: int, K: int, W: int) -> float:
        # 抽分得到的累计分范围 [K, K - 1 + W]
        if K == 0:
            return 1.0
        dp = [0.0] * (K + W)
        for i in range(K, min(N, K + W - 1) + 1):
            dp[i] = 1.0
        for i in range(K - 1, -1, -1):
            for j in range(1, W + 1):
                dp[i] += dp[i + j] / W
        return dp[0]

    def new21Game_error(self, N: int, K: int, W: int) -> float:
        """
        0 分开始，并在她的得分少于 K 分时抽取数字
            从 [1, W] 的范围中随机获得一个整数, 累计得分
        当不少于 K 分时，停止抽取数字。分数不超过 N 的概率是多少？
        :param N:
        :param K: 分数上限
        :param W: 抽取得分上限，无限次 完全背包
        """
        # 抽分得到的累计分范围 [K, K - 1 + W]
        if K - 1 + W <= N:
            return 1
        if K > N:  # 下限 > N
            return 0

        # 凑零钱，计算出 [1, K] 所有可行方案
        # [K-1, K-1+W] 依赖于之前的方案和，并且最后1个可选硬币的面值 有范围约束
        dp = [0] * (K + W)
        dp[0] = 1  # 对应从 0 转移的方案数

        # 计算出 [1, K] 所有可行方案
        for i in range(1, W + 1):
            for j in range(i, K + 1):
                dp[j] += dp[j - i]  # 子问题方案数, j-i 递增 对应不同子问题

        for j in range(K + 1, K + W):  # 剩下方案
            for k in range(K - 1, j - W - 1, -1):  # 可从之前的状态转移来
                dp[j] += dp[k]

        # for idx, num in enumerate(dp):
        #     print(idx, num)

        return sum(dp[K:N + 1]) / sum(dp[K:])


s = Solution()
# print(s.new21Game(10, 1, 10))
# print(s.new21Game(6, 1, 10))  # 6/10
print(s.new21Game(N=21, K=17, W=10))
