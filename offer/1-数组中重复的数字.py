"""
https://leetcode-cn.com/problems/shu-zu-zhong-zhong-fu-de-shu-zi-lcof/
面试题03. 数组中重复的数字
"""

# 长度为 n 的数组 nums
# 所有数字都在 0～n-1 的范围内
nums = [0, 1, 2, 3, 4, 11, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]


# 遍历数组，使用 set 存储，只有不同数字才能加入集合
# set 集合存储时先判断其 hashCode() 值是否一样，不一样直接存
# 时间 O(n), 空间 O(n)
def findRepeatNumber(nums):
    s = set()
    for v in nums:
        if v in s:
            return v
        else:
            s.add(v)
    return -1


# 排序，看相邻二值
# 时间 O(nlogn), 空间 O(1)
def findRepeatNumber2(nums):
    # 排序后，只比较相相邻的两个数字即可
    nums = sorted(nums)
    for v1, v2 in zip(nums[:-1], nums[1:]):
        if v1 == v2:
            return v1
    return -1


print(findRepeatNumber(nums))
print(findRepeatNumber2(nums))
