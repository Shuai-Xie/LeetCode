# LeetCode

Solve Problems on LeetCode by Python.

--- 
### 3. [无重复字符的最长子串](https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/solution/wu-zhong-fu-zi-fu-de-zui-chang-zi-chuan-by-leetcod/)
- 滑动窗口
- 查找用的 sub_str 可用 hashset， python 查找效率: set > dict > list
```py
def lengthOfLongestSubstring0(s):
    ll = 0  # 初始化 ll 可能长度，may have empty str
    for i in range(len(s)):
        sub_str = {s[i]}  # set
        while i + 1 < len(s) and s[i + 1] not in sub_str:
            sub_str.add(s[i + 1])
            i += 1
        # find a local max
        ll = max(len(sub_str), ll)
    return ll 
```
- 优化的滑动窗口
- 字典后来值 更新前值的原理，能向前看找到一个最近的重复值所在位置的下一位，进行字串长度比较
```py
def lengthOfLongestSubstring(s):
    st = {}
    i, ans = 0, 0
    for j in range(len(s)):
        if s[j] in st:
            i = max(i, st[s[j]])  # 更新后的起始位置 j+1
        ans = max(ans, j - i + 1)
        st[s[j]] = j + 1  # 字典后来值 更新前值的原理，能向前看找到一个最近的重复值所在位置的下一位
    return ans 
```

---
### 2. [两数相加](https://leetcode-cn.com/problems/add-two-numbers/)
- 链表初始化、遍历
- **哑结点是没有赋有效值的头结点**，可以用来保存 sum 链表的起始位置，方便 return
- 使用进位 carry 简化问题
- 活用 p, p.next，往往 while p: p = p.next

```py
# Definition for singly-linked list. 单向链表
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):  # l1, l2 is ListNode
        # set dummy head for sum linked list
        dummy_head = ListNode(0)  # 哑结点简化代码
        p, q, cur = l1, l2, dummy_head  # l1,l2 本身没有 dummy head
        carry = 0  # 进位 简化加法的过程
        while p or q:  # or 将2个链表都遍历完
            x = p.val if p else 0  # 完美解决其中1个list到头的问题，相当于在 list 左边位置赋 0
            y = q.val if q else 0
            sum = x + y + carry
            carry = sum // 10  # 更新进位，其实对于加法 carry = 1
            cur.next = ListNode(sum % 10)  # 这里是在给 l3 赋值
            cur = cur.next
            if p:  # 如果 p 是最后1个，那么 p.next=None,下一轮 while, p.val=0
                p = p.next
            if q:
                q = q.next
        if carry > 0:  # 遍历完后，判断最左侧是否还要加1
            cur.next = ListNode(carry)
        return dummy_head.next  # 从 sum 的最后1位开始

# 链表初始化
def init_ListNode(list):
    node = ListNode(list[0])  # 从 list 的 第1个元素开始
    p = node
    for i in range(1, len(list)):
        p.next = ListNode(list[i])
        p = p.next
    return node

# 链表遍历
def traverse(listnode):
    p = listnode
    while p:
        if p.next is None:  # 最后1个值
            print(p.val)
        else:
            print(p.val, end=',')
        p = p.next
```

---
### [matrix_chain_DP 矩阵链乘法 动态规划](https://blog.csdn.net/luoshixian099/article/details/46344175)
- 括号加的位置，影响着 链乘矩阵 整体的乘法计算次数
- 动态规划，大问题能建立在很多子问题上，而很多子问题是重复的，所以采用自底向上的方法，以空间换时间，将子问题的解存起来，比递归求解更快

```py
def matrix_chain_DP(matrixs):
    """
    :param matrixs: [rows-cols] of matrix chains
    :return: m: cost matrix, s: cut matrix
    """
    mat_num = len(matrixs) - 1  # 矩阵个数

    # 1 链 (A) i=j, m[i][i] = 0 没有乘法
    m = np.zeros((mat_num + 1, mat_num + 1), dtype=int)  # l chain 最优计算代价 min
    s = np.zeros((mat_num + 1, mat_num + 1), dtype=int)  # l chain 最优分割位置，索引要是 int

    # [i,j] 链乘子问题, i <= j, 上三角矩阵
    for l in range(2, mat_num + 1):  # 从 2 链 -> mat_num 链
        # l chain [i,j]  l=j-i+1
        for i in range(1, mat_num - l + 1 + 1):  # begin pos: 第1个矩阵 -> 第 mat_num - l + 1 个矩阵
            j = i + l - 1  # end pos 闭区间
            # sub chain of l chain
            for k in range(i, j + 1):  # 定义 chain 内分割点 k，从 i 到 j，A 右侧 cols
                # i-1: 对应 matrixs 第 i 个矩阵的 rows
                # k,j: 对应 matrixs 第 k,j 个矩阵的 cols
                # 如果要更明显的展示，可以将 matrixs 改写，不过从 1 开始的结果意义更明显
                q = m[i][k] + m[k][j] + matrixs[i - 1] * matrixs[k] * matrixs[j]
                if q < m[i][j] or m[i][j] == 0:  # 初始值 0，更新
                    m[i][j] = q
                    s[i][j] = k  # 设置 [i,j] 之间划分位置
    return m, s 
```
- 从结果来看，在合适位置添加括号，确实能减少整体乘法计算量

```
链乘矩阵: [30, 35, 15, 5, 10, 20, 25]
(1, 1) cost: 0       A1
(1, 2) cost: 15750   (A1A2)
(1, 3) cost: 5250    (A1(A2A3))
(1, 4) cost: 7500    ((A1(A2A3))A4)
(1, 5) cost: 9750    ((A1(A2A3))(A4A5))
(1, 6) cost: 10875   ((A1(A2A3))(A4(A5A6)))
(2, 2) cost: 0       A2
(2, 3) cost: 2625    (A2A3)
(2, 4) cost: 5125    ((A2A3)A4)
(2, 5) cost: 7625    ((A2A3)(A4A5))
(2, 6) cost: 8875    ((A2A3)(A4(A5A6)))
(3, 3) cost: 0       A3
(3, 4) cost: 750     (A3A4)
(3, 5) cost: 1500    (A3(A4A5))
(3, 6) cost: 1875    (A3(A4(A5A6)))
(4, 4) cost: 0       A4
(4, 5) cost: 1000    (A4A5)
(4, 6) cost: 1250    (A4(A5A6))
(5, 5) cost: 0       A5
(5, 6) cost: 5000    (A5A6)
(6, 6) cost: 0       A6
```

---

### [floor_heater 热水器楼层划分](https://www.jianshu.com/p/65d86c1f8231)

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