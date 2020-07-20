from typing import List


class Solution:
    def exchange(self, nums: List[int]) -> List[int]:
        # i 从左向右 寻找偶数
        # j 从右向左 寻找奇数
        # 并互相替换
        i, j = 0, len(nums) - 1
        while i < j:
            # 内部 while 寻找时，只要不满足 i<j 就说明找完了
            while i < j:
                if nums[i] % 2 == 0:  # 偶数
                    break
                i += 1
            while i < j:
                if nums[j] % 2:  # 奇数
                    break
                j -= 1
            # 找到左右两侧 奇数 偶数；替换
            nums[i], nums[j] = nums[j], nums[i]

        return nums
