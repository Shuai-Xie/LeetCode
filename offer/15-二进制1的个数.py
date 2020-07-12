class Solution:
    """
    输入整数，给出二进制1的个数
    """

    def hammingWeight(self, n: int) -> int:
        return sum([int(i) for i in '{:b}'.format(n)])

    def hammingWeight1(self, n: int) -> int:
        # 使用移位操作，每次比较最后1位是否为 1
        res = 0
        while n:
            res += n & 1  # 判断 n 最后1位是否为 1
            n = n >> 1  # 右移1位，判断下1个数
        return res

    def hammingWeight2(self, n: int) -> int:
        res = 0
        while n:
            res += 1
            n = n & (n - 1)  # 每次循环都能去掉 n 最右边的1，比 hammingWeight1 更高效
        return res


s = Solution()
print(s.hammingWeight2(9))
