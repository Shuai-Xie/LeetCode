"""1.两数之和
https://leetcode-cn.com/problems/two-sum/
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。

题目假设只有一组答案，暗示了 key 的单一性

哈希表
- 保持数组中的 每个元素与其索引相互对应的最好方法.
- Python dict 类型就是哈希表，key 不会相同，不用担心 hash 函数设计
- 通过以空间换取速度的方式，可以将查找时间从 O(n) 降低到 O(1)

哈希表支持以 “近似” 恒定的时间进行快速查找。
“近似”是因为一旦出现冲突，查找用时可能会退化到 O(n)。
但只要仔细地挑选哈希函数，在哈希表中进行查找的用时应当被摊销为 O(1)。

"""

nums = [100, 2, 7, 7, 15]
target = 9


def twoSum(nums, target):
    d = {}
    for idx, v in enumerate(nums):
        w = target - v
        if w in d:
            return [d[w], idx]
        d[v] = idx  # 记录下 v 的位置
    return None


print(twoSum(nums, target))


def twoSum1(nums, target):
    # O(nlogn) 排序 nlogn + 首尾递进查找 nlogn
    sorted_idx = sorted(range(len(nums)), key=lambda k: nums[k])
    # 先构建 idx 数组，再根据对应 idx num 值排序
    head = 0
    tail = len(nums) - 1
    sum_result = nums[sorted_idx[head]] + nums[sorted_idx[tail]]
    # 一增一减 保证顺序
    while sum_result != target:
        if sum_result > target:
            tail -= 1
        elif sum_result < target:
            head += 1
        sum_result = nums[sorted_idx[head]] + nums[sorted_idx[tail]]
    return [sorted_idx[head], sorted_idx[tail]]


def twoSum2(nums, target):
    # O(n^2) 6992 ms
    LEN = len(nums)
    # 思路和选择排序一样，按照这个索引思路，很容易设置运行时间很长的测试样例
    for i in range(LEN - 1):
        for j in range(i + 1, LEN):
            if nums[i] + nums[j] == target:
                return [i, j]
