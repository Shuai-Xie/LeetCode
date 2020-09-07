from typing import List

"""
输入：[1,2,2]
输出：1
解释：经过一次 move 操作，数组将变为 [1, 2, 3]。

move 操作: 选择任意1个数，+1
每次选中1个数，增加1，使得数组唯一

问需要执行的 move 次数
"""


class Solution:

    def minIncrementForUnique(self, A: List[int]) -> int:
        A.sort()

        # 数组唯一，判断严格增序的值 是否满足不等
        res = 0
        n = len(A)
        for i in range(n - 1):
            d = A[i + 1] - A[i]
            if d <= 0:  # 需要 move, 并更新 A[i+1]
                res += (-d + 1)
                A[i + 1] = A[i] + 1
        return res


s = Solution()
# A = [1, 2, 2]
A = [3, 2, 1, 2, 1, 7]
print(s.minIncrementForUnique(A))
