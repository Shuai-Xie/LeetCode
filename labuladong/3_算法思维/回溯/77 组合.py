"""
https://leetcode-cn.com/problems/combinations/
给定两个整数 n 和 k，返回 1 ... n 中所有可能的 k 个数的组合。
"""
from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        path = []

        # cur ~ [1, n]
        def dfs(cur):  # 当前位置
            pl = len(path)
            if pl + n - cur + 1 < k:  # 剪枝，即便剩下全遍历完 也无法得到长度 k
                return
            if pl == k:
                ans.append(path[:])
                return
            # 选择使用当前元素
            path.append(cur)
            dfs(cur + 1)
            path.pop()
            # 直接跳过当前元素
            dfs(cur + 1)

        dfs(1)
        return ans

    def combine_list(self, nums: List[int], k: int) -> List[List[int]]:
        """
        组合数判断规则：选择某个位置上的数字 使用还是直接跳过
        """
        ans = []
        path = []

        n = len(nums)

        def dfs(i):  # 当前遍历到的位置
            pl = len(path)
            if pl + n - i < k:  # 剪枝，即便剩下全遍历完 也无法得到长度 k
                return
            if pl == k:  # 某条搜索路径找到，后面的 nums 无需再判断，因为不会添加新元素了，只会引入空元素 带来重复
                ans.append(path[:])
                return
            # 使用当前元素
            path.append(nums[i])
            dfs(i + 1)
            path.pop()
            # 不用当前元素
            dfs(i + 1)

        dfs(0)
        return ans


s = Solution()
print(s.combine(3, 2))

nums = [1, 2, 3]
print(s.combine_list(nums, 2))
