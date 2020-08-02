"""
数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。可推理：超过一半的数字 必然是唯一的
你可以假设数组是非空的，并且给定的数组总是存在多数元素。
"""

from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        half = len(nums) / 2  # float 没关系，只要严格 >

        cnt = {}
        for v in nums:
            cnt[v] = cnt.get(v, 0) + 1  # 默认值=0
            if cnt[v] > half:
                return v


s = Solution()
print(s.majorityElement([1, 2, 3, 2, 2, 2, 5, 4, 2]))
