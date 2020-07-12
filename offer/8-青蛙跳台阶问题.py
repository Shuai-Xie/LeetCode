"""
https://leetcode-cn.com/problems/qing-wa-tiao-tai-jie-wen-ti-lcof/

一只青蛙一次可以跳上1级台阶，也可以跳上2级台阶。
求该青蛙跳上一个 n 级的台阶总共有多少种跳法。

动态规划问题

青蛙最后一步有 2 种情况: 1, 2
所以 f(n) = f(n-1) + f(n-2) 斐波那契数列，但 f(0)=1，因为 f(2)=2，与原始斐波那契不同
再反推倒数第2步 ...
"""


class Solution:
    def numWays(self, n: int) -> int:
        def fib(n):  # 0<=n<=100
            a, b = 1, 1
            for _ in range(n):  # 使用 a,b 保存中间结果
                a, b = b, a + b  # a 恰好为第 n 个数
            return a % 1000000007

        return fib(n)


a = Solution()

print(a.numWays(7))
