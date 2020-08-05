"""
输入一个整数 n ，求1～n这n个整数的十进制表示中1出现的次数。
例如，输入12，1～12这些整数中包含1 的数字有 1、10、11 和 12，1 一共出现了5次。
"""


class Solution:

    def countDigitOne(self, n: int) -> int:
        # 1 <= n < 2^31, 数量级很大，一定有规律
        res = 0

        # n_i 当前位的数字 cur [遍历对象]
        # n_i-1,...,n_1 低位 low
        # n_x,...,n_i+1 高位 high
        digit = 1  # 位因子，表示当前位为 个位
        cur = n % 10
        high = n // 10
        low = 0

        while high > 0 or cur > 0:  # 尚有高位 or 当前位不为0
            if cur == 0:
                res += high * digit  # 不存在以 cur 为首位的数
            elif cur == 1:  # 考虑 low
                res += high * digit + low + 1  # 存在 cur 为首位的数，但受 low 影响总数量
            else:  # cur>1
                res += high * digit + digit  # 存在，且不受 low 影响，即 cur 起始的 digit 位数字 都满足

            digit *= 10  # 升到十位
            cur = high % 10  # high 的最后1位 作为 cur
            high = high // 10  # high 左移
            low = n % digit

        return res

    def countDigitOne_long(self, n: int) -> int:
        # 超时，逐个数字判断，必然超时
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
