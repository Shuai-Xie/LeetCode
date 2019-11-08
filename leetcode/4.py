def findMedianSortedArrays(nums1, nums2):
    """
    找出这两个有序数组的中位数, 要求算法的时间复杂度为 O(log(m + n))
    :param nums1: 长度为 m 有序数组
    :param nums2: 长度为 n 有序数组
    :return: median
    """
    m, n = len(nums1), len(nums2)
    i, j = 0, 0
    # 归并成 1 个有序 list
    merge = []
    while i < m or j < n:
        if nums1[i] <= nums2[j]:
            merge.append(nums1[i])
            i += 1
        else:
            merge.append(nums2[j])
            j += 1
        # 终止条件
        if i < m and j == n:
            merge.extend(nums1[i:])
            break
        if i == m and j < n:
            merge.extend(nums2[j:])
            break

    # 奇偶放一起 计算 median
    return (merge[(m + n - 1) // 2] + merge[(m + n) // 2]) / 2


print(findMedianSortedArrays([1, 3], [2]))
print(findMedianSortedArrays([1, 2], [3, 4]))
