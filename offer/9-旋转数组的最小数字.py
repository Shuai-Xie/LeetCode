"""
把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。

输入一个递增排序的数组的一个旋转，输出旋转数组的最小元素。例如，数组 [3,4,5,1,2] 为 [1,2,3,4,5] 的一个旋转，该数组的最小值为1。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/xuan-zhuan-shu-zu-de-zui-xiao-shu-zi-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List

"""
递增排序的一个旋转，属于半有序数组
note: 别忽略 旋转 0 个元素的情况
"""


class Solution:
    # 二分法 O(n) -> O(log(n))
    def minArray(self, numbers: List[int]) -> int:
        i, j = 0, len(numbers) - 1

        while i <= j:
            m = (i + j) // 2  # 向下取整，i <= m < j

            if numbers[m] > numbers[j]:  # m 在左侧升序数组，min 在右边
                i = m + 1  # 跳过 m
            elif numbers[m] < numbers[j]:  # m 在右侧升序数组，min 在左边，todo:且有可能是最小的
                j = m
            else:  # 二者相等不好判断，实用 j-1 打破僵局
                j -= 1
        return numbers[i]

    def minArray1(self, numbers: List[int]) -> int:
        if len(numbers) > 1:
            for i in range(len(numbers) - 1):
                if numbers[i] > numbers[i + 1]:
                    return numbers[i + 1]
        return numbers[0]  # len(numbers) == 1, 或 旋转了0个元素

    def minArray2(self, numbers: List[int]) -> int:
        return sorted(numbers)[0]


# 递增旋转数组的 1个旋转
a = [3, 4, 5, 1, 2]

s = Solution()
print(s.minArray(a))
