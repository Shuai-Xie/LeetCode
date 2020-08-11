"""
返回不重复的全排列

输入: [1,1,2]
输出:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]
"""

from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        path = []
        used = [False] * n

        nums.sort()  # 先排序，同类元素会向量，剪枝好判断

        def dfs(depth):
            if depth == len(nums):  # 已经到最后一层
                res.append(path[:])  # copy path 对象
                return
            # n 数字顺序，恰好为字典序
            for i in range(n):
                # 用 used 保存每个 i 使用状态，不必每次到 path 中去查找
                if used[i]:  # 出现在 i 之前的元素
                    continue

                # 定义剪枝条件? 将 res 中已经出现的 前半段路径 相同的去掉?
                # not used[i - 1] 回溯回来 刚刚撤掉选择, 表明同值的必须是 同层的兄弟结点
                if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                    continue

                # 如果 i 还没用
                path.append(nums[i])
                used[i] = True  # note: 如果在这里将 所有同值元素置为 True，会导致循环完，树的长度达不到 n

                # 寻找下一个元素
                dfs(depth + 1)
                # 回溯，重置状态
                path.pop()  # 移除最后1个
                used[i] = False

        dfs(0)
        return res


s = Solution()
a = s.permuteUnique([1, 2, 5, 5, 5])
print(len(a))
print(a)
