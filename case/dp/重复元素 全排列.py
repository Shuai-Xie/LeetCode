"""
集合S中有n个元素，其中的元素可能重复，
设计一个算法，计算出S的不同排列字符 全部由小写字母组成
"""

import itertools


def demo():
    # a = [5, 5, 2, 1]
    a = [1, 2, 5, 5]
    # https://docs.python.org/2/library/itertools.html#itertools.permutations
    # Elements are treated as unique based on their position, not on their value.
    # Permutations are emitted in lexicographic sort order.
    # 字典序输出，但 key 是位置 idx，而不是具体的 value
    perm = list(itertools.permutations(a))  # 排列数，参数 r, A_4^r
    print(perm)
    print(len(perm))  # 24

    comb = []  # 不看顺序
    for i in range(1, len(a) + 1):
        comb += list(itertools.combinations(a, i))  # 组合数
    print(comb)
    print(len(comb))  # 15


# def permutations(iterable, r=None):
#     # r: 全排列数的个数
#     pool = tuple(iterable)
#     n = len(pool)
#     r = n if r is None else r
#     if r > n:
#         return
#
#     indices = list(range(n))
#     cycles = list(range(n, n - r, -1))  # [n, n-1, n-r+1]
#
#     res = []
#     res.append(tuple(pool[i] for i in indices[:r]))  # 下标的字典序
#
#     while n:
#         for i in reversed(range(r)):  # r 从高到 0
#             cycles[i] -= 1
#             if cycles[i] == 0:
#                 indices[i:] = indices[i + 1:] + indices[i:i + 1]
#                 cycles[i] = n - i
#             else:
#                 j = cycles[i]
#                 indices[i], indices[-j] = indices[-j], indices[i]
#                 res.append(tuple(pool[i] for i in indices[:r]))
#                 break
#     return res


def permutations(iterable, r=None):
    pool = tuple(iterable)
    n = len(pool)
    r = n if r is None else r
    if r > n:
        return
    indices = list(range(n))
    cycles = list(range(n, n - r, -1))
    yield tuple(pool[i] for i in indices[:r])
    while n:
        for i in reversed(range(r)):
            cycles[i] -= 1
            if cycles[i] == 0:
                indices[i:] = indices[i + 1:] + indices[i:i + 1]
                cycles[i] = n - i
            else:
                j = cycles[i]
                indices[i], indices[-j] = indices[-j], indices[i]
                yield tuple(pool[i] for i in indices[:r])
                break
        else:
            return


a = [1, 2, 5, 5]
print(list(permutations(a)))
