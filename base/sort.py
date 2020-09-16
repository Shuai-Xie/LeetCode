import numpy as np
from base.prime import generate_primes


# 排序的稳定性 针对元素对应的存储地址

## 插入排序

# 直接插入排序，泛化版，设置了 插入步长；稳定
def insert_sort(a, step=1):
    for i in range(step, len(a)):  # 从第2个元素开始插入
        j = i - step
        # 首先要判断 j 在范围内；即便第2项不满足，跳出时j=-1
        while j >= 0 and a[j] > a[i]:  # 倒序判断，严格 > 关系，当 = 跳出 while 排在 j+1，排序稳定
            j -= step
        if j < i - step:  # 需要插入排序的时候；不仅仅是交换二者位置，涉及二者之间元素位移
            a.insert(j + step, a.pop(i))  # 找到插入位置，pop i, insert j+1
    return a


# 希尔排序，不稳定，因为同一元素如果分在不同组，位置可能会变
def shell_sort(a):
    # https://blog.csdn.net/qq_42449106/article/details/103351581
    # Hibbard 增量: https://blog.csdn.net/weixin_40839812/article/details/78597127
    # 改进后的插入排序，又称缩小增量排序，算法效率受增量序列影响, Hibbard 增量 O(n^1.5)
    # 思想：每个 sub_list 都有序，即整个 list 基本有序的情况下，插入代价较小；当 step=1，退化为直接插入排序
    # 还未比较的元素往上层的已有序的 sub_list 中插入，从而减少元素比较次数，提高效率
    # todo: 排序步长尽量互质，不让如果 step 之间最大公约数如果 >1，则会在 step 较小的 sub_list 再次比较上层已经比较过的元素, Hibbard 增量
    steps = generate_primes(len(a) // 2)[::-1]  # reverse
    if steps[-1] != 1:
        steps.append(1)
    for step in steps:  # 下限是0，但不会到0
        print('step:', step)
        insert_sort(a, step)
    print(a)


# 选择排序
def select_sort(arr):
    # 从小到大，往后面找 存在更小的就交换
    n = len(arr)
    for i in range(n - 1):  # 保证每个位置 i 的元素都是 最小的
        for j in range(i + 1, n):
            if arr[j] < arr[i]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr


# 冒泡排序
def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):  # i=0, j+1
            if arr[j] > arr[j + 1]:  # 比较两个连续的值；将最大值不断确定
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


# 快排
def quick_sort(arr):
    n = len(arr)
    if n <= 1:
        return arr

    left, right = 0, n - 1
    pivot = arr[left]  # 枢轴

    while left < right:
        while left < right and arr[right] >= pivot:
            right -= 1
        arr[left], arr[right] = arr[right], arr[left]  # 枢轴交换到右侧 idx=right
        while left < right and arr[left] <= pivot:
            left += 1
        arr[left], arr[right] = arr[right], arr[left]

    # 枢轴位置 left
    arr[:left] = quick_sort(arr[:left])
    arr[left + 1:] = quick_sort(arr[left + 1:])  # 枢轴位置已确定，所以从 left+1 开始

    return arr


# 归并排序
def merge_sort(arr):
    n = len(arr)
    if n <= 1:
        return arr

    # 左右排序
    mid = n // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    # 归并
    res = []
    i, j = 0, 0
    while i < mid and j < n - mid:
        if left[i] < right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1
    return res + left[i:] + right[j:]

    # pop 简洁，但存取多
    # while left and right:
    #     if left[0] < right[0]:
    #         res.append(left.pop(0))
    #     else:
    #         res.append(right.pop(0))
    # return res + left + right


# 堆排序
# 从前向后截取，不断构建小顶堆
def heap_sort(arr):
    n = len(arr)
    if n <= 1:
        return arr

    # 利用完全二叉树，父节点 与 子节点 idx 关系；自下而上构建 小顶堆; 保证孩子比父节点大
    for i in range(n // 2, -1, -1):
        if 2 * i + 1 < n and arr[2 * i + 1] < arr[i]:  # 左
            arr[2 * i + 1], arr[i] = arr[i], arr[2 * i + 1]
        if 2 * i + 2 < n and arr[2 * i + 2] < arr[i]:  # 右
            arr[2 * i + 2], arr[i] = arr[i], arr[2 * i + 2]
    arr[1:] = heap_sort(arr[1:])
    return arr


if __name__ == '__main__':
    a = list(np.random.permutation(30))
    print(a)
    # print(quick_sort(a[:]))
    # print(bubble_sort(a[:]))
    # print(merge_sort(a[:]))
    print(heap_sort(a[:]))
