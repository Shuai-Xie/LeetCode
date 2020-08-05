from typing import List
import functools


class Solution:
    """
    输入 非负数组，拼起来得到 最小数
    - 输出结果可能非常大，所以你需要返回一个字符串而不是整数
    - 拼接起来的数字可能会有前导 0，最后结果不需要去掉前导 0

    0 < nums.length <= 100

    核心：等位数下，数字的优先级排列
    字符串 xy < yx，说明 **在位数一定的数中** x排在y的前面，通过排序排出一个前面后面优先级

    字符串排序 判断规则 二元操作符
    - 若 x+y > y+x, 则 y 应在前; 反之 x 在前, 如此，对 nums 转成 str val 进行排序
    - 排序后的 传递性证明
    """

    def minNumber(self, nums: List[int]) -> str:
        # 数字是一个整体，不能拆分为 单个数
        strs = [str(n) for n in nums]
        # 使用内部函数，自定义比较的 key
        # cmp_to_key 定义了 list 中元素之间的 对比关系；如果直接 lambda 只有1个元素
        strs.sort(key=functools.cmp_to_key(lambda x, y: 1 if x + y > y + x else -1))
        return ''.join(strs)

    def minNumber2(self, nums: List[int]) -> str:
        nums = list(map(str, nums))

        # 自己实现快排
        def fast_sort(nums):
            if len(nums) <= 1:  # 注意 0,1 两种情况
                return nums

            pivot = nums[0]
            left, right = 0, len(nums) - 1
            while left < right:
                # 寻右
                while left < right and nums[right] + pivot >= pivot + nums[right]:  # right > pivot
                    right -= 1  # 找到第一
                # 交换 pivot 到右侧，保证 右侧都 >= pivot
                nums[left], nums[right] = nums[right], nums[left]

                # 寻左
                while left < right and nums[left] + pivot <= pivot + nums[left]:  # left <= pivot
                    left += 1
                # left 与 pivot 交换，保证左侧都 < pivot
                nums[left], nums[right] = nums[right], nums[left]

            # 当 left=right，pivot 所在位置 已确定
            nums[:left] = fast_sort(nums[:left])
            nums[left + 1:] = fast_sort(nums[left + 1:])
            return nums

        return ''.join(fast_sort(nums))


s = Solution()
print(s.minNumber([10]))
print(s.minNumber([10, 2]))
print(s.minNumber([3, 30, 34, 5, 9]))

print(s.minNumber2([10]))
print(s.minNumber2([10, 2]))
print(s.minNumber2([3, 30, 34, 5, 9]))
