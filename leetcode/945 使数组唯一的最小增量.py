from typing import List

"""
输入：[1,2,2]
输出：1
解释：经过一次 move 操作，数组将变为 [1, 2, 3]。

move 操作: 选择任意1个数，+1
每次选中1个数，增加1，使得数组唯一
"""


class Solution:
    def minIncrementForUnique(self, A: List[int]) -> int:
        A.sort()
        n = len(A)
        f = [0] * n

        if n == 0 or n == 1:
            return 0

        for i in range(1, n):
            d = A[i] - A[i - 1]
            if d <= 0:
                f[i] = f[i - 1] + 1 - d  # 变成严格比之前大的
                A[i] += 1 - d  # 直接更新掉这个值
            else:
                f[i] = f[i - 1]

        return f[-1]


s = Solution()
# A = [1, 2, 2]
A = [3, 2, 1, 2, 1, 7]
print(s.minIncrementForUnique(A))
