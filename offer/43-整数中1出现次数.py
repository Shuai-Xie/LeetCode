"""
输入一个整数 n ，求1～n这n个整数的十进制表示中1出现的次数。
例如，输入12，1～12这些整数中包含1 的数字有 1、10、11 和 12，1 一共出现了5次。
"""


class Solution:

    def countDigitOne(self, n: int) -> int:
        # 1 <= n < 2^31, 数量级很大，一定有规律
        digit = 1  # 个位
        res = 0
        high, cur, low = n // 10, n % 10, 0

        while high != 0 or cur != 0:

        return res

    def countDigitOne_long(self, n: int) -> int:
        # 超时
        arr = [str(a) for a in range(1, n + 1)]
        cnt = 0
        for s in arr:
            cnt_s = 0
            for c in s:
                if c == '1':
                    cnt_s += 1
            cnt += cnt_s
        return cnt


s = Solution()
print(s.countDigitOne(12))
