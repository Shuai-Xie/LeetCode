from typing import List


# 快排 每个分治 能找到数组中 第k个最大元素
# 可帮助 缩小选择区间
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if not nums:
            return
        left, right = 0, len(nums) - 1
        pivot = nums[left]
        while left < right:
            while left < right and nums[right] >= pivot:
                right -= 1
            # 小值交换到 pivot 左侧
            nums[left], nums[right] = nums[right], nums[left]
            while left < right and nums[left] <= pivot:
                left += 1
            # 大值交换到 pivot 右侧
            nums[left], nums[right] = nums[right], nums[left]
        # 找到 pivot 所在位置为 left
        if left == len(nums) - k:  # 注意是 第 k 大, 转成第 k 小
            return nums[left]
        elif left > len(nums) - k:  # 第 k 大 要从右边查
            return self.findKthLargest(nums[:left], left - (len(nums) - k))
        else:
            return self.findKthLargest(nums[left + 1:], k)

    def quickSort(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        nums = nums[:]  # 避免改变原 list
        left, right = 0, len(nums) - 1
        pivot = nums[left]
        while left < right:
            while left < right and nums[right] >= pivot:
                right -= 1
            # 小值交换到 pivot 左侧
            nums[left], nums[right] = nums[right], nums[left]
            while left < right and nums[left] <= pivot:
                left += 1
            # 大值交换到 pivot 右侧
            nums[left], nums[right] = nums[right], nums[left]
        # left = right
        nums[:left] = self.quickSort(nums[:left])
        nums[left + 1:] = self.quickSort(nums[left + 1:])
        return nums


s = Solution()
# nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
# k = 4
nums = [3, 2, 1, 5, 6, 4]
k = 2
print(s.quickSort(nums))
print(s.findKthLargest(nums, k))
