def f(n):
    """
    严重超时, 200 就要算很久
    大量重复的递归计算，例如 f(n) 和 f(n - 1) 两者向下递归需要 各自计算 f(n−2) 的值。
    """
    if n == 0 or n == 1:
        return n
    else:
        val = f(n - 2) + f(n - 1)
        return val % 1000000007


class Solution:
    """
    f(n) = f(n-1) + f(n-2)
    """

    def fib(self, n: int) -> int:
        a, b = 0, 1
        for _ in range(n):  # 使用 a,b 保存中间结果
            a, b = b, a + b  # a 恰好为第 n 个数
        return a % 1000000007


s = Solution()
print(s.fib(45))
