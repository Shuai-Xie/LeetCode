"""
地上有一个m行n列的方格，从坐标 [0,0] 到坐标 [m-1,n-1] 。
一个机器人从坐标 [0, 0] 的格子开始移动，
    它每次可以向左、右、上、下移动一格（不能移动到方格外），
    也不能进入行坐标和列坐标的数位之和大于k的格子。
例如，当 k 为18时，机器人能够进入方格 [35, 37] ，因为3+5+3+7=18。
但它不能进入方格 [35, 38]，因为3+5+3+8=19。请问该机器人能够到达多少个格子？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/ji-qi-ren-de-yun-dong-fan-wei-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


def sums(x):  # 转成 str 分离数字 求和
    return sum([int(c) for c in str(x)])


def sums2(x):  # // 10 从末尾相加
    s = 0
    while x != 0:
        s += x % 10
        x = x // 10
    return s


class Solution:
    """
    1 <= n,m <= 100  不可能遍历 2D 坐标系所有坐标位置，计算是否 < k，设想 1000000000? 崩
    0 <= k <= 20     robot 去 DFS 行走?
    """

    def movingCount(self, m: int, n: int, k: int) -> int:
        """
        :param m: 行数
        :param n: 列数
        :param k: 数位和上限
        :return: 总共可到的格子数量
        """

        def cal_next_num_sum(next_num, cur_num):
            """
            :param next_num: 下一数字
            :param cur_num: 当前数字 数位和
            :return:
            """
            return cur_num + 1 if next_num % 10 else cur_num - 8

        visited = set()  # 递归所以定义全局

        def dfs(i, j, s):
            """
            :param i: 当前位置
            :param j:
            :param s: 当前数位和
            :return: 可以走过的步数
            """
            if i < m and j < n and s <= k and (i, j) not in visited:
                visited.add((i, j))
            else:
                return 0

            return 1 + dfs(i + 1, j, cal_next_num_sum(i + 1, s)) + dfs(i, j + 1, cal_next_num_sum(j + 1, s))

        def bfs():
            queue = [(0, 0, 0)]  # i,j,s
            visited = set()  # 内部即可
            while queue:  # 队列不为空
                i, j, s = queue.pop(0)
                if i < m and j < n and s <= k and (i, j) not in visited:
                    visited.add((i, j))
                else:
                    continue  # note: 一定要保留循环出口；如果不是可达点，后面 queue 就添加了

                # 广度优先搜索 两个方向；入队列后 再在下次循环判断是否是可达点
                queue.append((i + 1, j, cal_next_num_sum(i + 1, s)))
                queue.append((i, j + 1, cal_next_num_sum(j + 1, s)))

            return len(visited)

        # steps = dfs(0, 0, 0)
        steps = bfs()
        return steps


s = Solution()
print(s.movingCount(2, 3, 1))
