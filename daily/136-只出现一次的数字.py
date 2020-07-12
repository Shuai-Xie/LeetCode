"""
https://leetcode-cn.com/problems/single-number/submissions/
给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。
线性时间复杂度，并且不使用额外空间

如果使用额外空间，字典的查找也是 O(n), 因为找 v
数组中查询1个数字是否出现是 O(n)

排序后，再查找是 O(nlog(n)) + O(n)
"""
import collections

# d = collections.defaultdict(lambda: 0)  # 定义每个 value 初始值为 0

nums = [4, 1, 2, 1, 2]


# 如果可用额外空间 O(n)
def singleNumber1(nums):
    d = {}
    for v in nums:
        d[v] = 1 if v not in d else d[v] + 1

    for k, v in d.items():
        if v == 1:
            return k


# 不使用额外空间
def singleNumber(nums):
    d = nums[0]
    for v in nums[1:]:
        d ^= v
    return d


"""
采用异或运算
1. a^b^c = a^c^b 满足交换律，数组元素位置不影响最终结果
2. a^a = 0 去掉数组中相同数字
3. a^0 = a 保留数组中单一元素

同或：a⊙b=ab+a'b'
异或：a^b=a'b+ab'
互为逆运算
"""


def demo():
    print(0 ^ 4)  # 4
    print(4 ^ 4)  # 0
    print(4 ^ 2)  # 6
    print(4 ^ 2 ^ 4)  # 2


print(singleNumber(nums))
