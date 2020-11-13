class Solution:
    def fib(self, N: int) -> int:
        """
        f(N) = f(N-1) + f(N-2)
        """
        if N == 0 or N == 1:
            return N
        a, b = 0, 1
        for i in range(2, N + 1):  # 要执行到 N
            a, b = b, a + b
        return b


s = Solution()
for i in range(10):
    print(s.fib(i), end=' ')
