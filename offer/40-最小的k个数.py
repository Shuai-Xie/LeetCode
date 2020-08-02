"""
输入整数数组 arr ，找出其中最小的 k 个数。例如，输入4、5、1、6、2、7、3、8这8个数字，则最小的4个数字是1、2、3、4。

不要求按顺序输出
"""
from typing import List


# def quick_sort2(arr):
#     if len(arr) < 2:
#         return arr
#
#     left, right = [], []
#     mid = arr[len(arr) // 2]
#     arr.remove(mid)
#
#     for v in arr:
#         if v <= mid:
#             left.append(v)
#         else:
#             right.append(v)
#
#     return quick_sort2(left) + [mid] + quick_sort2(right)
#
#
# def partition(arr, low, high):
#     pivot = arr[low]  # 随便取 数列首元素位 枢轴，划分元素到左右
#
#     while low < high:
#         # 设置 pivot 为 low，先 high 才能实现二者替换
#         while low < high and arr[high] >= pivot:
#             high -= 1
#         arr[low], arr[high] = arr[high], arr[low]  # a[low] 枢轴替换到 a[high]
#
#         # 如果 low 在前，替换的并不是 枢轴的值
#         while low < high and arr[low] <= pivot:
#             low += 1
#         arr[low], arr[high] = arr[high], arr[low]  # a[high] 枢轴替换到 a[low]
#
#     return low  # 枢轴元素 所在位置


# def partition(arr, low, high):
#     i = (low - 1)  # 最小元素索引
#     pivot = arr[high]
#
#     for j in range(low, high):
#         # 当前元素小于或等于 pivot
#         if arr[j] <= pivot:
#             i += 1  # 对应当前 j 所在 elem
#             arr[i], arr[j] = arr[j], arr[i]
#
#     arr[i + 1], arr[high] = arr[high], arr[i + 1]
#     return i + 1  # arr[high] 是 pivot，所以最终 pivotLoc = i+1
#
# def quick_sort(arr, low, high):
#     if low < high:  # 递归终止条件，当不满足时，表示不需要排序
#         # 虽然可以合并位1个函数，但是 partition 独立出来更清晰
#         pivLoc = partition(arr, low, high)  # 分治
#         quick_sort(arr, low, pivLoc - 1)  # 注意 low, high
#         quick_sort(arr, pivLoc + 1, high)


class Solution:
    """
    取出最小的 k 个数
    1. 快排 寻找下标为 k-1 的数, 左侧的数都 < 枢轴值
    2. 堆排序，小根堆，k 次取堆顶
    3. 排序 + 截取
    4.
    """

    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        if not arr or k == 0 or k > len(arr):
            return []

        def partition(low, high):
            pivot = arr[low]  # 随便取 数列首元素位 枢轴，划分元素到左右

            while low < high:
                # 设置 pivot 为 low，先 high 才能实现二者替换
                while low < high and arr[high] >= pivot:
                    high -= 1
                arr[low], arr[high] = arr[high], arr[low]  # a[low] 枢轴替换到 a[high]

                # 如果 low 在前，替换的并不是 枢轴的值
                while low < high and arr[low] <= pivot:
                    low += 1
                arr[low], arr[high] = arr[high], arr[low]  # a[high] 枢轴替换到 a[low]

            return low  # 枢轴元素 所在位置

        def quick_search(low, high):
            pivotLoc = partition(low, high)  # 不管 low,high 为多少, pivotLoc 对应全局位置
            if pivotLoc == k - 1:
                return arr[:k]
            # > 左侧, < 右侧
            return quick_search(low, pivotLoc - 1) if pivotLoc > k - 1 else quick_search(pivotLoc + 1, high)

        return quick_search(0, len(arr) - 1)

    def getLeastNumbers3(self, arr: List[int], k: int) -> List[int]:
        return sorted(arr)[:k]

    def getLeastNumbers4(self, arr: List[int], k: int) -> List[int]:
        # 冒泡排序，将 len(arr) - k 个最大数排好;
        # O(n^2) 超出时间限制
        for i in range(len(arr) - k):
            for j in range(0, len(arr) - i - 1):  # 末次: (0, len(arr)-k), 恰好到 [0,k-1] 之后全是较大数
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
        return arr[:k]


s = Solution()
# arr, k = [3, 2, 1], 2
arr, k = [0, 0, 0, 2, 0, 5], 1
print(s.getLeastNumbers(arr, k))
print(s.getLeastNumbers3(arr, k))
