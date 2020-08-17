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


## 选择排序

# 简单选择排序
def select_sort(a):
    LEN = len(a)
    for i in range(LEN):
        for j in range(i + 1, LEN):
            if a[i] > a[j]:  # swap(i,j)
                a[i], a[j] = a[j], a[i]  # 最小元素放前
    return a


# 堆排序
# 利用完全二叉树，父子节点 idx 位置关系，构建大根堆
# 并不断将最大值替换到数组末尾
def heap_sort(a):
    LEN = len(a)
    if LEN == 1:
        return a
    else:
        # 自下而上 建立大根堆；从最后1个父亲 idx = (LEN-1 -1)//2 开始直到 root
        for i in range((LEN - 2) // 2, -1, -1):  # 反过来就是堆中idx最大的左孩子位置
            child = 2 * i + 1  # 左孩子; idx 不是从1开始的
            if child + 1 < LEN:  # 判断是否有 右孩子
                child = child + 1 if a[child + 1] > a[child] else child  # 指向最大孩子
            if a[child] > a[i]:  # 交换 父子
                a[i], a[child] = a[child], a[i]
        # 建完大根堆后，更换首尾
        a[0], a[LEN - 1] = a[LEN - 1], a[0]
        # 递归构建剩下的元素，成为大根堆
        a[:-1] = heap_sort(a[:-1])  # 排序结果更新原来 list
        return a


## 交换排序

# 冒泡排序，最大值放后
def bubble_sort(a):
    LEN = len(a)
    for i in range(1, LEN):
        for j in range(LEN - i):  # 上限 LEN-2
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    return a


# 快速排序，递归
# 自上而下 根据 pivot 分割 sub_list
# 所以 quick_sort 分割左右在后，而 merge_sort 在前
def quick_sort(a):
    a = a[:]  # 不改变原序列
    if len(a) <= 1:  # 也要处理空 list，比如下面 low=0
        return a
    low, high = 0, len(a) - 1
    pivot = a[low]  # 基准值
    while low < high:
        # 两边往中间查找
        while low < high and a[high] >= pivot:  # 不用担心条件1先不满足，因为 low=high，赋值无影响
            high -= 1
        a[low], a[high] = a[high], a[low]  # 把 < pivot 的值 a[high] 放左边，此时 a[low] = pivot
        while low < high and a[low] <= pivot:
            low += 1
        a[low], a[high] = a[high], a[low]  # 把 > pivot 的值 a[low] 放右边，此时 a[high] = pivot
    # low 为 pivot 实际位置
    # 再分别排序左右
    a[:low] = quick_sort(a[:low])  # 截取相当于 重新初始化了?
    a[low + 1:] = quick_sort(a[low + 1:])
    return a


# 归并排序
# 自下而上 归并 sub_list 为有序
def merge_sort(a):
    if len(a) < 2:
        return a
    else:
        mid = len(a) // 2  # 平分两段，要避免最下端 array 只有 2个元素时，始终分不开为2个长度为1的list的问题
        # 递归将 merge 两段 都排成有序，再 归并
        a[:mid] = merge_sort(a[:mid])
        a[mid:] = merge_sort(a[mid:])
        b = []
        i, j = 0, mid
        while i < mid and j < len(a):
            if a[i] < a[j]:
                b.append(a[i])
                i += 1
            else:
                b.append(a[j])
                j += 1
        b = b + a[i:mid] + a[j:]
        return b


def merge_sort2(arr):
    n = len(arr)
    if n < 2:
        return arr
    else:
        mid = n // 2  # 均分两段
        a = merge_sort2(arr[:mid])  # 不断分解到最短 len(a) = 0 or 1
        b = merge_sort2(arr[mid:])
        # 此时 a,b 两段已有序
        c = []
        while a and b:
            if a[0] < b[0]:
                c.append(a.pop(0))
            else:
                c.append(b.pop(0))
        c = c + a + b  # 其中1个必为空 []
        return c


if __name__ == '__main__':
    a = list(np.random.permutation(12))
    print(a)
    print(quick_sort(a))
    print(a)
    print(merge_sort2(a))
    print(a)
    print(merge_sort(a))
