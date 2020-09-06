class Solution:
    """
    设绳子长度为 x, 段数 m = n/x
    y = x^(n/x)
    将 y 转换成 e^(ln(x) * n/x) 求导
        1 - ln(x) = 0, x = 2-3
        2^(1/2) < 3^(1/3), 所以 x = 3 取最优
    """

    def cuttingRope(self, n: int) -> int:
        if n == 2:
            return 1
        if n == 3:
            return 2

        def cal_product(base):
            res = 1
            while base > 0:
                res = res * 3 % (1e9 + 7)
                base -= 1
            return res

        base, remain = n // 3, n % 3
        if remain == 0:
            res = cal_product(base)
        elif remain < 3 / 2:
            res = cal_product(base - 1) * 4 % (1e9 + 7)
        else:
            res = cal_product(base) * 2 % (1e9 + 7)
        return int(res)


s = Solution()
print(s.cuttingRope(10))
