from typing import List


class Solution:
    # 统计一个数字在排序数组中出现的次数
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return 0
        if nums[-1] < target or nums[0] > target:
            return 0

        cnt = 0
        for v in nums:
            if v == target:
                cnt += 1
            elif v > target:
                return cnt

    def search2(self, nums: List[int], target: int) -> int:
        # return nums.count(target)

        # 有序数列 二分查找
        if len(nums) == 0:
            return 0
        if nums[-1] < target or nums[0] > target:
            return 0

        left, right = 0, len(nums) - 1
        mid = 0
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:  # 已经找到头的情况下 与 target 不等
                break
            elif nums[mid] > target:  # 划边界时 直接将 mid 排除在外
                right = mid - 1
            else:
                left = mid + 1

        if nums[mid] == target:
            cnt = 1
            # 左搜
            tmp = mid
            while mid > 0:
                mid -= 1
                if nums[mid] == target:
                    cnt += 1
                else:
                    break
            # 右搜, 注意左搜时 mid 已经变化，要用 tmp 保留
            mid = tmp
            while mid < len(nums) - 1:
                mid += 1
                if nums[mid] == target:
                    cnt += 1
                else:
                    break
            return cnt
        else:
            return 0


s = Solution()
nums = [5, 7, 7, 8, 8, 10]
# target = 8
target = 6

# nums = [1, 4]
# target = 1
print(s.search(nums, target))
print(s.search2(nums, target))
