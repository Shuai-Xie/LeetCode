from typing import List


def cmp(a, b):
    if a > b:
        return 1
    elif a < b:
        return -1
    else:
        return 0


class Solution:

    def maxTurbulenceSize(self, A: List[int]) -> int:
        # 内存 O(1), 时间 O(n)
        n = len(A)
        ans = 1
        i = 0  # 双指针 左

        for j in range(1, n):  # 双指针 右
            c = cmp(A[j - 1], A[j])  # current j 是否合法
            if j == n - 1 or c * cmp(A[j], A[j + 1]) != -1:  # 末尾 or 不满足，截断 更新 i
                if c != 0:  # c=0 不处理，直接跳过，因为 c=0 对应的 ij 长度=1
                    ans = max(ans, j - i + 1)
                i = j
        return ans

    def maxTurbulenceSize_dp(self, A: List[int]) -> int:
        # 内存/时间 都是 O(n)
        if max(A) == min(A):
            return 1




    def maxTurbulenceSize_old(self, A: List[int]) -> int:
        """
        要求必须是 连续的，可以用 双指针 滑窗
        """
        n = len(A)
        if n <= 1:
            return n
        if n == 2:  # 特殊情况
            return 1 if A[0] == A[1] else 2

        res = 1  # 至少为 1
        i = 0 if A[0] != A[1] else 1  # 起始位置

        for j in range(2, n):  # i=0时，从第3个元素开始判断后序关系
            if cmp(A[j], A[j - 1]) * cmp(A[j - 1], A[j - 2]) == -1:  # 正确情况
                if j == n - 1:  # 已经是最后一个了; 其他情况不做处理 继续 iter
                    res = max(res, n - i)
            else:  # 不满足，截断了
                base = j - i
                if A[j - 1] == A[j - 2]:  # 判断前2个是否也不满足
                    base -= 1
                res = max(res, base)
                i = j - 1  # 更新 新的起始位置

        return res


s = Solution()
# nums = [9, 4, 2, 10, 7, 8, 8, 1, 9]
# nums = [4, 8, 12, 16]
# nums = [9, 9, 9]
# nums = [100, 100, 100]
# nums = [0, 8, 45, 88, 48, 68, 28, 55, 17, 24]
# nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
# nums = [9, 4, 2, 10, 7, 8, 8, 1, 9]
nums = [4, 8, 12, 16]

print(s.maxTurbulenceSize(nums))
print(s.maxTurbulenceSize_dp(nums))
