"""
给定一个 没有重复 数字的序列，返回其所有可能的全排列。
"""
from typing import List


class Solution:
    # dfs 回溯: 回到之前状态的意思
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []

        # 回溯过程 就是保存 决策树的搜索路径
        used = [False] * n
        path = []

        def dfs(d):  # 当前树的深度，也即全排列第i个位置可选的元素
            nonlocal path
            if d == n:
                ans.append(path)
                return

            for i in range(n):
                # 排除不合法的选择
                if used[i]:  # 如果此元素之前已添加，不可再用
                    continue
                # 做选择
                path.append(nums[i])
                used[i] = True
                # 进入下一层决策树
                dfs(d + 1)  # 当首层为 i 情况遍历完后; 下一轮首个状态变为 nums[i+1], 元素 i 又变为未使用状态
                # 取消选择
                path = path[:-1]
                used[i] = False

        dfs(0)
        return ans

    def permute2(self, nums: List[int]) -> List[List[int]]:
        """
        去除全排列过程中 遇到的重复结果
        """
        n = len(nums)
        ans = []

        # 回溯过程 就是保存 决策树的搜索路径
        used = [False] * n
        path = []

        nums = sorted(nums)  # 排序后的数组

        def dfs(d):  # 当前树的深度，也即全排列第i个位置可选的元素
            nonlocal path
            if d == n:
                ans.append(path)
                return

            for i in range(n):
                # 排除不合法的选择
                if used[i]:  # 如果此元素之前已添加，不可再用
                    continue
                # 与不存在重复的相比，多一层 情况过滤，判断哪些状况是 节点重复状态
                if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                    # 因为 i == i-1;
                    # 如果 not used[i-1]，表示当前节点 i-1 刚刚判断完回来; 同层路径遇到了重复元素, 砍掉
                    # 如果 used[i-1]; 表示正在向深层递归时，遇到了重复元素; 保留
                    continue

                # 当前深度，做选择
                path.append(nums[i])
                used[i] = True
                # 进入下一层决策树
                dfs(d + 1)  # 当首层为 i 情况遍历完后; 下一轮首个状态变为 nums[i+1], 元素 i 又变为未使用状态
                # 撤销选择
                path = path[:-1]
                used[i] = False

        dfs(0)
        return ans


s = Solution()
a = s.permute([1, 2, 2])
print(len(a))
print(a)
a = s.permute2([1, 2, 2])
print(len(a))
print(a)
