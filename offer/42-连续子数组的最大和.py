"""
输入一个整型数组，数组里有正数也有负数。
数组中的一个或连续多个整数组成一个子数组。求所有子数组的和的最大值。
要求时间复杂度为O(n)。

"""
from typing import List


class Solution:
    """
    nums 存在 正负，求子数组中 最大的和
       1 <= arr.length <= 10^5
    -100 <= arr[i] <= 100
    """

    def maxSubArray(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        # dp[0] = max(0, nums[0])  # 负数肯定不选, arr.length >= 1
        dp[0] = nums[0]  # 子数组暗含了不为空
        curmax = dp[0]
        for i in range(1, len(nums)):
            # 状态转移 只有两种情况 +nums[i] 或者 不加
            dp[i] = max(dp[i - 1] + nums[i], nums[i])
            curmax = max(curmax, dp[i])

        return curmax


s = Solution()
print(s.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
print(s.maxSubArray([-2, -1, -3]))
