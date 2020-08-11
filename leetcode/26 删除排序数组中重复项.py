"""
给定一个排序数组, 原地删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。
不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。
"""
from typing import List


class Solution:
    # 快慢指针
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return n
        i = 0
        for j in range(1, n):
            if nums[j] > nums[i]:  # 不等
                i += 1  # 与 j 同增
                nums[i] = nums[j]  # 快指针取到的值 赋给 慢指针所在位置

        nums = nums[:i + 1]  # 替换完 截取即可
        print(nums)
        return i + 1  # 长度

    def removeDuplicates_me(self, nums: List[int]) -> int:
        # O(n^2) 删除元素也是 O(n)
        n = len(nums)
        if n < 2:
            return n

        s = 1  # 对应 nums[0]
        i = 1
        while i < n:
            if nums[i] > nums[i - 1]:  # 比 != 更快
                s += 1
                i += 1
            else:
                nums.pop(i)
                n -= 1
        print(nums)
        return s


s = Solution()
# a = [1, 1, 2]
a = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
print(s.removeDuplicates(a))
