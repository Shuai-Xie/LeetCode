# LeetCode

Solve Problems on LeetCode by Python.

---
2.[两数相加](https://leetcode-cn.com/problems/add-two-numbers/)



---

1.[两数之和](https://leetcode-cn.com/problems/two-sum/)

- **哈希查找** O(1)
- 哈希表是保持数组中的 每个元素与其索引相互对应的最好方法.
- 通过以空间换取速度的方式，可以将查找时间从 O(n) 降低到 O(1)
- Python dict 就是哈希表，key 不会相同


```py
def twoSum(self, nums, target):
    
    hashmap = {}  # python dict is hashmap
    for index, num in enumerate(nums):
        another_num = target - num
        if another_num in hashmap:
            return [hashmap[another_num], index]

        # add num to dict {num: idx}
        # 题目假定输入只对应1个答案，所以不会出现 num 相同，即 key 唯一
        # 对 dict 而言，即便 key 相同，后来 num 的 idx 也会更新前者的 idx，即同一 num 的 idx 会变大
        hashmap[num] = index
    return None
```

- **首尾递进查找** O(nlogn) = 排序 O(nlogn) + 首尾递进查找 O(n)

```py
def twoSum(self, nums, target):
    # 先构建 idx 数组，再根据对应 idx 的 num 值排序，得到从小到大 num 对应的 idx 位置
    sorted_idx = sorted(range(len(nums)), key=lambda k: nums[k])
    head = 0
    tail = len(nums) - 1
    sum_result = nums[sorted_idx[head]] + nums[sorted_idx[tail]]
    while sum_result != target:
        if sum_result > target:  # 慢慢变小
            tail -= 1
        elif sum_result < target:  # 慢慢变大
            head += 1
        sum_result = nums[sorted_idx[head]] + nums[sorted_idx[tail]]
    return [sorted_idx[head], sorted_idx[tail]] 
```