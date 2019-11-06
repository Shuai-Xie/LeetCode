"""1.两数之和
https://leetcode-cn.com/problems/two-sum/

哈希表
- 保持数组中的 每个元素与其索引相互对应的最好方法.
- Python dict 类型就是哈希表，key 不会相同
- 通过以空间换取速度的方式，可以将查找时间从 O(n) 降低到 O(1)

哈希表支持以 “近似” 恒定的时间进行快速查找。
“近似”是因为一旦出现冲突，查找用时可能会退化到 O(n)。
但只要仔细地挑选哈希函数，在哈希表中进行查找的用时应当被摊销为 O(1)。

"""

nums = [100, 2, 7, 7, 15]
target = 9


class Solution:
    def twoSum(self, nums, target):
        # O(1) 52 ms
        hashmap = {}  # python dict is hashmap
        for index, num in enumerate(nums):
            another_num = target - num
            if another_num in hashmap:
                return [hashmap[another_num], index]

            # 添加 num: index 到 dict
            # 因为题目假设只有一组答案，即便两个数字重复，即 key 都 = num
            # 对于存 dict 而言，后来者会更新前者的 index，但是此程序直接找到后就会 return
            hashmap[num] = index
        return None

    def twoSum1(self, nums, target):
        # O(nlogn) 排序 nlogn + 首尾递进查找 nlogn
        sorted_idx = sorted(range(len(nums)), key=lambda k: nums[k])
        # 先构建 idx 数组，再根据对应 idx num 值排序
        head = 0
        tail = len(nums) - 1
        sum_result = nums[sorted_idx[head]] + nums[sorted_idx[tail]]
        while sum_result != target:
            if sum_result > target:
                tail -= 1
            elif sum_result < target:
                head += 1
            sum_result = nums[sorted_idx[head]] + nums[sorted_idx[tail]]
        return [sorted_idx[head], sorted_idx[tail]]

    def twoSum2(self, nums, target):
        # O(n^2) 6992 ms
        LEN = len(nums)
        # 思路和选择排序一样，按照这个索引思路，很容易设置运行时间很长的测试样例
        for i in range(LEN - 1):
            for j in range(i + 1, LEN):
                if nums[i] + nums[j] == target:
                    return [i, j]


print(Solution().twoSum(nums, target))
