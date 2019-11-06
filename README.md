# LeetCode

Solve Problems on LeetCode by Python.

---
### 2. [两数相加](https://leetcode-cn.com/problems/add-two-numbers/)


---
### [热水器楼层划分](https://www.jianshu.com/p/65d86c1f8231)

- 组合数 选出所有可能放置情况，再选择双成本最小的
- 组合数 时间复杂度接近阶乘: https://www.zhihu.com/question/38474425/answer/76641611
- **还没想到一个更快的方法。虽然能找出一些情况的较快解法，但不适用所有情况**

```py
def best_heater_floors(floors, heaters):
    """
    满足 2 个约束条件：
        1. 每层楼的人打热水时，上下楼层最少
        2. 热水器放置总楼层数之和最小，即安放成本最小
    在能满足 1 的情况下满足 2，先按 1 排序 再按 2
    :param floors: 楼层总数
    :param heaters: 热水器数量
    :return: heater_floors 热水器放置的楼层
    """
    # 可能的放置情况，从中选取
    cand_heater_floors = list(itertools.combinations(range(1, floors + 1), heaters))
    total_step_floors = []  # idx corresponds to idx in cand_heater_floors
    for heater_floors in cand_heater_floors:
        # each heaters
        total_steps = 0  # sum of min_step of each person
        total_floors = sum(heater_floors)
        for p in range(1, floors + 1):  # 1-5
            # each person's floor - each heater's floor
            min_step = min([abs(p - h) for h in heater_floors])
            total_steps += min_step
        total_step_floors.append((total_steps, total_floors))

    # 双成本最小的
    heater_floors = cand_heater_floors[total_step_floors.index(min(total_step_floors))]
    return heater_floors 
```

---

### 1. [两数之和](https://leetcode-cn.com/problems/two-sum/)

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

    # 题目假定了一定有一组解，所以这样肯定可以查找到
    # 注意：并不能设置提前终止条件！因为 left + right 之和并不一定是单调的
    while sum_result != target:
        if sum_result > target:  # 慢慢变小
            tail -= 1
        elif sum_result < target:  # 慢慢变大
            head += 1
        sum_result = nums[sorted_idx[head]] + nums[sorted_idx[tail]]
    return [sorted_idx[head], sorted_idx[tail]] 
```