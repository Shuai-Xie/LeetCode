import numpy as np


# matrix chain, 括号加的位置，影响着整体乘法计算次数
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
                # 如果要更明显的展示，可以将 matrixs 改写，不过有从 1 开始的结果意义更明显
                q = m[i][k] + m[k][j] + matrixs[i - 1] * matrixs[k] * matrixs[j]
                if q < m[i][j] or m[i][j] == 0:  # 初始值 0，更新
                    m[i][j] = q
                    s[i][j] = k  # 设置 [i,j] 之间划分位置
    # print(m)
    # print(s)
    return m, s


def print_chain_order(s, i, j):
    """
    :param s: cut matrix
    :param i: idx of begin matrix in matrix chain
    :param j: idx of end matrix in matrix chain
    """
    if i == j:
        print('A{}'.format(i), end='')
    else:
        print('(', end='')
        print_chain_order(s, i, s[i][j])  # left cut
        print_chain_order(s, s[i][j] + 1, j)  # right cut 闭区间
        print(')', end='')


def print_each_ij_cost(m, s):
    # 实际在动规的顺序，是按照 L 逐渐增长，从 1-mat_num 有不同组合
    mat_num = m.shape[0] - 1
    for i in range(1, mat_num + 1):
        for j in range(i, mat_num + 1):
            print('({}, {}) cost: {:<8}'.format(i, j, m[i][j]), end='')
            print_chain_order(s, i, j)
            print()


if __name__ == '__main__':
    matrixs = [30, 35, 15, 5, 10, 20, 25]
    m, s = matrix_chain_DP(matrixs)
    print_chain_order(s, 1, 6)
    print()
    print(matrixs)
    print_each_ij_cost(m, s)
