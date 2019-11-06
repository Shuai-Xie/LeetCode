# LeetCode

Solve Problems on LeetCode by Python.

---
2.[两数相加](https://leetcode-cn.com/problems/add-two-numbers/)



---

1.[两数之和](https://leetcode-cn.com/problems/two-sum/)


- **哈希表**是保持数组中的 每个元素与其索引相互对应的最好方法.
- Python dict 类型就是哈希表，key 不会相同
- 通过以空间换取速度的方式，可以将查找时间从 O(n) 降低到 O(1)

```py
def twoSum(self, nums, target):
    # O(1) 52 ms
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