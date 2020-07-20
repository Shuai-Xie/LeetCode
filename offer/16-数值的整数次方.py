class Solution:
    def myPow(self, x: float, n: int) -> float:
        """
        二分递归相乘，不过仍然有大量重复运算
        :param x:
        :param n: 指数；注意考虑 指数为负的情况
        :return:
        """
        # 考虑 正负 n %2 的 mod
        if n == 1 or n == 0 or n == -1:
            return x ** n
        half = self.myPow(x, n // 2)
        mod = n % 2  # 没必要调用 myPow, 因为余数并不大
        return half * half * x ** mod

    def myPow1(self, x: float, n: int) -> float:
        """
        :param x: -100 < x < 100 注意分析 x=0 情况
        :param n: 注意分析 负指数情况
        :return:
        """
        if x == 0:
            return 0
        if n < 0:
            x, n = 1 / x, -n
        res = 1
        while n:  # 指数
            if n & 1:  # 奇数
                res *= x
            x *= x  # 内部 x 不断被 x**2 更新，没有大量重复运算
            n >>= 1  # 右移一位, /2
        return res


s = Solution()
print(s.myPow(2, -10))
print(1 / 1024)
