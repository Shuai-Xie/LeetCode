from typing import List


class Solution:
    # 递增排序
    def missingNumber(self, nums: List[int]) -> int:
        if nums[0] != 0:  # 如果是首个
            return 0
        if nums[-1] != len(nums):  # 如果是末个
            return nums[-1] + 1
        # 如果在中间
        for i in range(len(nums) - 1):
            if nums[i + 1] - nums[i] == 2:
                return nums[i] + 1
