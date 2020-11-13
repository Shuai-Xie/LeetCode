"""
a^b 对 1337 取模, a 正整数，b 是非常大的正整数(十进制)，以数组形式给出
示例 1:
输入: a = 2, b = [3]
输出: 8

示例 2:
输入: a = 2, b = [1,0]
输出: 1024

与之前题目相比，不仅要快速计算幂，还要在计算过程中 对模值 判断
"""
from typing import List


class Solution:
    def superPow(self, a: int, b: List[int]) -> int:

        def quickPow(x, n, m):
            """
            :param x: 底数
            :param n: 指数
            :param m: 模值
            :return:
            """
            ans = 1
            while n > 0:
                if n & 1 == 1:  # 等价于 n%2
                    ans = ans * x % m
                x = x * x % m
                n = n >> 1
            return ans

        res = 1
        m = 1337
        for i in b:
            # 第1项，上一步的解 作为底数，指数 = 10
            # 第2项，a 为底数，指数 = 遍历数组的元素    在计算1/2项时，都可用快速幂降到O(logn)
            # res = 第1项 * 第2项
            res = (quickPow(res, 10, m) * quickPow(a, i, m)) % m
            # 模公式
            # (a*b) % m = ((a%m) * (b%m)) % m
        return res
