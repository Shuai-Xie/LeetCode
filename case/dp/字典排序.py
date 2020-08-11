# 字典序排序
def alphabet_order_cmp(a, b):
    """
    返回 >0，表示 a>b; =0, a=b; <0, a<b
    """
    # 不按照长度? 就按照字母表顺序，谁先查到返回谁
    n = min(len(a), len(b))
    for i in range(n):
        if a[i] > b[i]:
            return 1
        elif a[i] < b[i]:  # =情况 继续向后遍历
            return -1

    if len(a) > n:  # 相等情况下, b 更长
        return 1
    elif len(b) > n:
        return -1  # a<b
    else:
        return 0


import functools

arr = [(1, 4), (1, 2, 3), (1, 4), (2, 1), (0, 100)]
b = sorted(arr, key=functools.cmp_to_key(alphabet_order_cmp))  # 这样 sorted 不会改变 arr 原值
print(b)
c = sorted(arr)
print(c)
