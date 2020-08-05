class Solution:
    # 序列化的字符串 数字序列，找到第 n 位数字
    # 0 <= n < 2^31
    def findNthDigit(self, n: int) -> int:
        if n == 0:
            return 0

        i = 0  # 表示数位个数
        s = 0  # 指定数字位数，对应最高为 第 s 位
        while s < n:
            i += 1
            s += i * 9 * 10 ** (i - 1)  # i 位数字 总个数

        # 跳出时，找到第 n 个数 所在的 i 位数区间
        begin = 10 ** (i - 1)  # 对应位数 数字的 最小值
        pos = i * 9 * 10 ** (i - 1) - (s - n)  # 正向位置
        # 按位置 和 数位个数 i 寻数
        base, remain = pos // i, pos % i

        val = begin + base - 1  # 注意：begin 已经是 第1个数了
        if remain == 0:
            return val % 10
        else:
            # 第 remain 位
            val += 1
            return val // 10 ** (i - remain) % 10


s = Solution()
print(s.findNthDigit(3))
print(s.findNthDigit(11))
