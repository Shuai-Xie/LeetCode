class Solution:
    def new21Game(self, N: int, K: int, W: int) -> float:
        """
        0 分开始，并在她的得分少于 K 分时抽取数字
            从 [1, W] 的范围中随机获得一个整数, 累计得分
        当不少于 K 分时，停止抽取数字。分数不超过 N 的概率是多少？
        :param N:
        :param K: 分数上限
        :param W: 抽取得分上限，无限次
        """
        # 抽分得到的累计分范围 [K, K - 1 + W]
        if K - 1 + W <= N:
            return 1
        if K > N:  # 下限 > N
            return 0

        # for v in range(K, K + W): # 背包容量，恰好放满, 求方案数

        dp = [0.] + [-float('inf')] * (K + W - 1)  # 容量上限 K+W-1
        # 保证所有结果 都从 0 转移

        # 凑零钱
        for i in range(1, K + W):  # 背包容量
            for j in range(1, min(i, W) + 1):
                dp[i] = max(dp[i], dp[i - j] + 1)

        print(dp)


s = Solution()
# print(s.new21Game(10, 1, 10))
print(s.new21Game(6, 1, 10))  # 6/10
# print(s.new21Game(21, 17, 10))
