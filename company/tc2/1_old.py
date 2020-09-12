"""
3
9
5 4 3 2 1 2 3 4 5
5
1 2 3 4 5
14

87 70 17 12 14 86 61 51 12 90 69 89 4 65
87 70 12 12 69 89
不要求连续

8
0
6
"""


def longest_subarr(arr):
    n = len(arr)
    dp = [1] * n

    for i in range(1, n):
        for j in range(i - 1, -1, -1):
            if arr[j] < arr[i]:
                dp[i] = dp[j] + 1
                break
    return max(dp)


def count_val(arr):
    # 不管 arr 是否 sort, 查询每个数出现次数，用 dict，O(n)
    val_cnts = {}  # val 出现次数
    val_idxs = {}  # val idxs 记录

    for idx, val in enumerate(arr):
        val_cnts[val] = val_cnts.get(val, 0) + 1
        if val not in val_idxs:
            val_idxs[val] = [idx]
        else:
            val_idxs[val].append(idx)

    return val_cnts, val_idxs


def get_longest(arr):
    # 递减 递增，并且 不要求 连续, 并且是 偶数长度
    val_cnts, val_idxs = count_val(arr)
    # 取出 val_cnt < 2 的元素，得到 candidate begin val
    # 对于 val_cnt > 2 的元素，不能仅根据 idx 到 mid 的位置选择保留哪些
    # 但一个优化的点在于：不需要组合数 C_n^2 判断，只要连续 2个 判断即可
    # 反证法: 12,12 如果另一个12出现在两侧，最优的仍然时连续的2值
    cand_begin_vals = []
    for val, cnt in list(val_cnts.items()):  # python3 迭代器类型不能遍历时修改，转成 list
        if cnt >= 2:
            cand_begin_vals.append(val)

    # 对于 idx 的出现位置，可做判断
    cand_begin_vals.sort()
    n = len(cand_begin_vals)

    # 将出现在 较小起始值外围 起始值 过滤掉
    del_flag = [False] * n
    for i in range(n - 1):
        if del_flag[i]:  # 一旦在遍历中指定 i 要删除，那么比 i 差的必然也在上轮判断出来了，不需要再比较
            continue
        idxs = val_idxs[cand_begin_vals[i]]
        min_left, max_right = min(idxs), max(idxs)
        for j in range(i + 1, n):  # 后面的值都是比 i 大的，如果 idx 分布在 i 外围，去掉
            idxs = val_idxs[cand_begin_vals[j]]
            mleft, mright = min(idxs), max(idxs)
            if mleft < min_left and mright > max_right:
                del_flag[j] = True

    cand_begin_vals = [cand_begin_vals[i] for i in range(n) if not del_flag[i]]

    def left_right_find(arr, left, right):
        return min(longest_subarr(arr[:left + 1][::-1]), longest_subarr(arr[right:])) * 2

    # b 中元素 从小到大
    # b[i+1] > b[i]，如果 i+1 所在的2个位置 在 i 所在位置两侧，可以直接忽略
    # O(n^2) 判断

    res = 0
    for val in cand_begin_vals:
        idxs = val_idxs[val]
        # 由于 相同元素的2个位置的 位置不易确定，所以逐个比较
        for left, right in zip(idxs[:-1], idxs[1:]):
            # 因为 val 是递增的，如果不满足 在较小 val 的内部，不需要考虑
            res = max(res, left_right_find(arr, left, right))
    return res


demos = [
    [5, 4, 3, 2, 1, 2, 3, 4, 5],
    [1, 2, 3, 4, 5],
    [87, 70, 17, 12, 14, 86, 61, 51, 12, 90, 69, 89, 4, 65]
]
for arr in demos:
    print(get_longest(arr))
