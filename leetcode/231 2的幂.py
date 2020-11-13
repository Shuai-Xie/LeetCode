class Solution:
    def isPowerOfTwo_me(self, n: int) -> bool:
        """
        判断整数 n 是否为 2 的幂，肯定是正数次幂，因为输入是整数
        """
        if n <= 0:  # 负数和0肯定不是
            return False
        if n == 1:
            return True
        while n > 1:
            n, r = n // 2, n % 2
            if n == 1 and r == 0:  # 除到最后的 2
                return True
            if r != 0:
                return False

    def isPowerOfTwo(self, n: int) -> bool:
        """ & 运算判断
        因为 2 的幂 表现为二进制必为: 10*
             如 n = 10000
              n-1 = 01111
        n & (n-1) = 00000 = 0
        """
        return n > 0 and n & (n - 1) == 0


s = Solution()
print(s.isPowerOfTwo(1))
print(s.isPowerOfTwo(16))
print(s.isPowerOfTwo(218))
