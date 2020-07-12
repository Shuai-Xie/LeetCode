"""
判断在一个矩阵中是否存在一条包含某字符串所有字符的路径。
路径可以从矩阵中的任意一格开始，每一步可以在矩阵中向左、右、上、下移动一格。
如果一条路径经过了矩阵的某一格，那么该路径不能再次进入该格子。

例如，在下面的3×4的矩阵中包含一条字符串“bfce”的路径（路径中的字母用加粗标出）。

[["a","b","c","e"],
["s","f","c","s"],
["a","d","e","e"]]

但矩阵中不包含字符串“abfb”的路径，因为字符串的第一个字符b占据了矩阵中的第一行第二个格子之后，路径不能再次进入这个格子。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/ju-zhen-zhong-de-lu-jing-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import List
import numpy as np

"""
矩阵中路径搜索：深度优先搜索 DFS + 剪枝
    DFS: 通过递归，先朝一个方向搜到底，再回溯至上个节点，沿另一个方向搜索，以此类推
    剪枝: 提前预见不能成功的路径；如:
            1.字符不同 [1,3可以归1类]
            2.索引越界
            3.字符已被访问
         立即返回到上一节点
    
    定义 DFS 4向 搜索顺序为：↓,↑,→,←
    使用 / 标记已经访问过的元素
    
时间复杂度：
    矩阵: M*N, word 字母总数 K；复杂度 O(3^K * M * N)
    总共可能有 M * N 个搜索起点
    确定一条路径后，每个 char 有 4 个方向，舍去来路方向，还剩 3 个，所以是 3^K
空间复杂度：
    O(K)，只存储 寻找到的 字符串长度
"""


class Solution_Error:

    def exist(self, board: List[List[str]], word: str) -> bool:
        board = np.array(board)

        def create_flag_board(m, n):
            # 为区域添加外围 boarder，直接根据 flags 值判断能否走，而不用考虑不同位置的方向
            upper = [-1] * (n + 2)
            mid = [-1] + [0] * n + [-1]
            flags = np.array([
                upper,
                *([mid] * m),  # * 拆出构建的二维矩阵，变成每一行
                upper
            ])
            return flags  # 类型跟随 list 内容

        def find_next_char_in_board(c, pos, flags):
            bi, bj = pos  # pos in board 当前位置
            fi, fj = bi + 1, bj + 1  # pos in flags
            # 下一步可能位置
            # 左
            if flags[fi][fj - 1] == 0 and board[bi][bj - 1] == c:  # 左边有效
                return True, (bi, bj - 1)
            # 右
            if flags[fi][fj + 1] == 0 and board[bi][bj + 1] == c:  # 右边有效
                return True, (bi, bj + 1)
            # 上
            if flags[fi - 1][fj] == 0 and board[bi - 1][bj] == c:  # 上边有效
                return True, (bi - 1, bj)
            # 下
            if flags[fi + 1][fj] == 0 and board[bi + 1][bj] == c:  # 下边有效
                return True, (bi + 1, bj)

            return False, None

        # board 二维矩阵
        if board.size > 0:
            m, n = board.shape

            # 所有可能的起始位置
            begin_pos = []
            for i in range(m):
                for j in range(n):
                    if board[i][j] == word[0]:
                        begin_pos.append((i, j))

            # 遍历每个起始位置
            for pos in begin_pos:
                path = [pos]
                flags = create_flag_board(m, n)
                flags[pos[0] + 1][pos[1] + 1] = 1  # 此位置已走过, 不能再走, list 对象 这样做会将所有行的此列赋为 1

                for idx, c in enumerate(word[1:]):  # 剩下 chars
                    find, pos = find_next_char_in_board(c, pos, flags)  # 找到 next pos，同时更新当前 pos
                    if not find:
                        break  # 这条路走不通 todo: 并不一定走不通，因为下一个 char 所在位置可能有多个，需要尝试多条起始路径；递归？
                    else:
                        path.append(pos)
                        flags[pos[0] + 1][pos[1] + 1] = 1  # 此位置已走过

                if len(path) == len(word):
                    # print('path:', path)
                    return True

        return False


class Solution_old:

    def exist(self, board: List[List[str]], word: str) -> bool:
        board = np.array(board)

        def create_flag_board(m, n):
            # 为区域添加外围 boarder，直接根据 flags 值判断能否走，而不用考虑不同位置的方向
            upper = [-1] * (n + 2)
            mid = [-1] + [0] * n + [-1]
            flags = np.array([
                upper,
                *([mid] * m),  # * 拆出构建的二维矩阵，变成每一行
                upper
            ])
            return flags  # 类型跟随 list 内容

        def find_next_char_in_board(c, pos, flags):
            bi, bj = pos  # pos in board 当前位置
            fi, fj = bi + 1, bj + 1  # pos in flags
            # 下一步可能位置
            next_pos = []
            # 左
            if flags[fi][fj - 1] == 0 and board[bi][bj - 1] == c:  # 左边有效
                next_pos.append((bi, bj - 1))
            # 右
            if flags[fi][fj + 1] == 0 and board[bi][bj + 1] == c:  # 右边有效
                next_pos.append((bi, bj + 1))
            # 上
            if flags[fi - 1][fj] == 0 and board[bi - 1][bj] == c:  # 上边有效
                next_pos.append((bi - 1, bj))
            # 下
            if flags[fi + 1][fj] == 0 and board[bi + 1][bj] == c:  # 下边有效
                next_pos.append((bi + 1, bj))

            return next_pos

        # 拿到起始点后，寻找一条完整子路径
        def find_all_path(begin_pos, word, flags):  # 给定起始位置，递归寻找完整路径
            if len(word) == 0:  # 已经找完了
                return True

            if len(word) > 0:
                next_pos = find_next_char_in_board(word[0], begin_pos, flags)
                if len(next_pos) == 0:
                    return False
                else:
                    for pos in next_pos:
                        # 每个 pos 更新的 flags 矩阵不同
                        tmp_flags = flags.copy()  # deep copy
                        tmp_flags[pos[0] + 1][pos[1] + 1] = 1  # 路径更新，当前位置已经走了
                        ret = find_all_path(pos, word[1:], tmp_flags)  # 随着递归深入，tmp_flags ?
                        if ret:
                            return True
            return False

        # board 二维矩阵
        if board.size > 0:
            m, n = board.shape

            # 所有可能的起始位置
            begin_pos = []
            for i in range(m):
                for j in range(n):
                    if board[i][j] == word[0]:
                        begin_pos.append((i, j))

            # 遍历每个起始位置
            for pos in begin_pos:
                flags = create_flag_board(m, n)
                flags[pos[0] + 1][pos[1] + 1] = 1  # 此位置已走过, 不能再走, list 对象 这样做会将所有行的此列赋为 1

                ret = find_all_path(pos, word[1:], flags)
                if ret:
                    return True

        return False


class Solution:
    """
    提示: 不同担心 board 为空
        1 <= board.length <= 200
        1 <= board[i].length <= 200
    """

    def exist(self, board: List[List[str]], word: str) -> bool:

        # 递归程序 一般先定义出口，再定义一般情况
        def dfs(i, j, k):  # 矩阵位置 (i,j), 搜索 word 位置 k
            # 越界 | 不等
            if not 0 <= i < len(board) or not 0 <= j < len(board[0]) or board[i][j] != word[k]:
                return False
            # dfs 终点
            if k == len(word) - 1:
                return True
            # 找到 word 中间的字母
            #   tmp 保存以防此路不通，之后恢复 /
            #   / 将访问过 char 转成 不等字母，归化条件 1
            tmp, board[i][j] = board[i][j], '/'
            # 四方查询
            res = dfs(i + 1, j, k + 1) or dfs(i - 1, j, k + 1) or dfs(i, j + 1, k + 1) or dfs(i, j - 1, k + 1)
            # 不管结果如何，回溯 char
            #   res=True, 找到终点，回溯每条路径
            #   res=False, dfs 失败，此路不通，放回替换为 / 的原始 char
            board[i][j] = tmp

            return res

        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i, j, 0):
                    return True

        return False

    def exist_and_record_path(self, board: List[List[str]], word: str) -> bool:
        paths = []

        def dfs(i, j, k):
            """
            :param i: 行号
            :param j: 列号
            :param k: word 当前 char 的编号
            :return:
            """
            # 越界 or 不等 [1,3 归 1]，return False
            if not 0 <= i < len(board) or not 0 <= j < len(board[0]) or board[i][j] != word[k]:
                return False
            # 如果上述条件都不满足，且 k 是最后一个，找到了
            if k == len(word) - 1:  # 注意 word 直接使用了外部函数的参数 word
                paths.append((i, j))  # 保存最后 1 个 char 路径，因为最后1个 char 通过时，程序没有执行到 paths.append 那里
                return True
            # 如果是中间字符，即找到了，那么要更新 i,j 在 board 中的 char 为 /，这样能将 3 归到 1 情况
            # (1) 假设走了当前路
            tmp, board[i][j] = board[i][j], '/'
            paths.append((i, j))  # 保存路径

            # 搜索 4 方: ↓,↑,→,← code 中不是3方，因为不确定来路方向
            res = dfs(i + 1, j, k + 1) or dfs(i - 1, j, k + 1) or dfs(i, j + 1, k + 1) or dfs(i, j - 1, k + 1)
            # (2) 当前路走不通，放回字母，表示此路不走 （回溯）
            # 假如选择了 E，发现 E 的下一步无路可走，即 dfs 无法再深度搜索
            # 3个 or 很巧妙，当 dfs = True，直接返回 True，找完了，立即回溯
            if not res:  # 此路不同，去掉这个路径
                paths.pop(len(paths) - 1)

            board[i][j] = tmp

            return res

        # M*N 个起点
        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i, j, 0):
                    print(paths)
                    return True

        return False

    # todo: 保存能搜索到的 最长 char 的位置
    def record_longest_path(self, board: List[List[str]], word: str) -> bool:
        all_paths = []
        paths = []

        def path_word(paths):
            return ''.join([board[i][j] for i, j in paths])

        def dfs(i, j, k):
            """
            :param i: 行号
            :param j: 列号
            :param k: word 当前 char 的编号
            :return:
            """
            # 越界 or 不等 [1,3 归 1]，return False
            if not 0 <= i < len(board) or not 0 <= j < len(board[0]) or board[i][j] != word[k]:
                return False
            # 如果上述条件都不满足，且 k 是最后一个，找到了
            if k == len(word) - 1:  # 注意 word 直接使用了外部函数的参数 word
                paths.append((i, j))  # 保存最后 1 个 char 路径，因为最后1个 char 通过时，程序没有执行到 paths.append 那里
                all_paths.append(paths)
                return True
            # 如果是中间字符，即找到了，那么要更新 i,j 在 board 中的 char 为 /，这样能将 3 归到 1 情况
            # (1) 假设走了当前路
            tmp, board[i][j] = board[i][j], '/'
            paths.append((i, j))  # 保存路径

            # 搜索 4 方: ↓,↑,→,← code 中不是3方，因为不确定来路方向
            res = dfs(i + 1, j, k + 1) or dfs(i - 1, j, k + 1) or dfs(i, j + 1, k + 1) or dfs(i, j - 1, k + 1)
            # (2) 当前路走不通，放回字母，表示此路不走 （回溯）
            # 发现一条未完成路径，添加到 all_paths 中
            if not res:
                all_paths.append(paths)

            board[i][j] = tmp

            return res

        # M*N 个起点
        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i, j, 0):
                    print(paths)
                    return True

        for p in all_paths:
            print(p)
            print(path_word(p))

        return False


if __name__ == '__main__':
    s = Solution()

    board = [["A", "B", "C", "E"],
             ["S", "F", "E", "S"],
             ["A", "D", "E", "E"]]
    # print(s.exist(board, "ABCESEEEFS"))
    # print(s.exist_and_record_path(board, 'ED'))
    # print(s.record_longest_path(board, 'ADEM'))
    print(s.record_longest_path(board, 'ED'))

    # board = [["a", "b", "c", "e"],
    #          ["s", "f", "c", "s"],
    #          ["a", "d", "e", "e"]]
    # print(s.exist(board, 'bfce'))
    # print(s.exist(board, 'abfb'))
