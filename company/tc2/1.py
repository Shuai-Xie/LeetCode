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


# arr = [5, 4, 3, 2, 1, 2, 3, 4, 5]
# arr = [1, 2, 3, 4, 5]
# arr = [87, 70, 17, 12, 14, 86, 61, 51, 12, 90, 69, 89, 4, 65]
# 选择增加的数 可以是 后面的...


def find_val_idxs(arr, v):
    res = []
    for i in range(len(arr)):
        if arr[i] == v:
            res.append(i)
    return res


def count_val(arr, v):
    cnt = 0
    for val in arr:
        if val == v:
            cnt += 1
        else:
            if cnt > 0:
                break
    return cnt


def longest_subarr(arr):
    n = len(arr)
    dp = [1] * n

    for i in range(1, n):
        for j in range(i - 1, -1, -1):
            if arr[j] < arr[i]:
                dp[i] = dp[j] + 1
                break
    return max(dp)


def get_longest(arr, n):
    # 递减 递增，并且 不要求 连续, 并且是 偶数长度
    # 中心两边搜索法
    # 从最小的数 位置出发 向两边找?
    a = arr[:]
    a.sort()
    # 从最小值开始寻找
    b = [v for v in a if count_val(a, v) >= 2]
    b = sorted(set(b))

    def left_right_find(arr, left, right):
        return min(longest_subarr(arr[:left + 1][::-1]), longest_subarr(arr[right:])) * 2

    res = 0
    for val in b:
        idxs = find_val_idxs(arr, val)
        for left, right in zip(idxs[:-1], idxs[1:]):
            # 因为 val 是递增的，如果不满足 在较小 val 的内部，不需要考虑
            res = max(res, left_right_find(arr, left, right))
    return res


T = int(input())
res = []
for _ in range(T):
    n = int(input())
    a = list(map(int, input().split()))
    res.append(get_longest(a, n))

for v in res:
    print(v)
