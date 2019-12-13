def findMedianSortedArrays1(nums1, nums2):
    """
    找出两个有序数组的中位数, 如果先归并，时间复杂度为 O(m + n)
    :param nums1: 长度为 m 有序数组
    :param nums2: 长度为 n 有序数组
    :return: median
    """
    m, n = len(nums1), len(nums2)
    i, j = 0, 0
    # 因为 nums1,nums2 本就有序，所以就是归并的 merge 操作
    # 归并成 1 个有序 list
    merge = []
    while i < m and j < n:
        if nums1[i] <= nums2[j]:
            merge.append(nums1[i])
            i += 1
        else:
            merge.append(nums2[j])
            j += 1

    merge.extend(nums1[i:])
    merge.extend(nums2[j:])

    # 奇偶放一起 计算 median
    # m+n 为奇数时，二者相等；为偶数时，恰为中间俩
    return (merge[(m + n - 1) // 2] + merge[(m + n) // 2]) / 2


def findMedianSortedArrays(nums1, nums2):
    """
    找出两个有序数组的中位数, 如果先归并，时间复杂度为 O(log(m + n))
    首先，要能明确 i,j 之间是有等式关系的；所以搜索的范围其实是在 i 之内；而后再考虑二分搜索
    :param nums1: 长度为 m 有序数组
    :param nums2: 长度为 n 有序数组
    :return: median
    """
    m, n = len(nums1), len(nums2)
    if m > n:  # 保证 m<=n，确保 i 对 j 在 nums2 中位置的影响
        nums1, nums2, m, n = nums2, nums1, n, m
    if n == 0:
        raise ValueError

    # i 划分点的范围，对 nums1 划分，可以在 nums1 头部[nums1 全在 right] 也可在尾部 [nums1 全在 left]
    imin, imax, half_len = 0, m, (m + n + 1) // 2
    # i+j = m-i + n-j +1, 保证了当 m+n 为奇数时，左侧元素总数比右侧多1，median 在 左侧
    while imin <= imax:  # 在此范围内，二分查找 i,j 划分点
        # 先满足 均分两段
        i = (imin + imax) // 2
        j = half_len - i
        # 当 i 处于划分点内部时，才可比较 left,right 切分后的值
        # 通过指定 i 的范围，同时确保了 i,j 都在合理范围内
        if i > 0 and nums1[i - 1] > nums2[j]:  # i>0 推出 j<n
            imax -= 1  # i 太大，调整上界
        elif i < m and nums2[j - 1] > nums1[i]:  # i<m 推出 j>0
            imin += 1  # i 太小，调整下界
        else:  # 恰如其分，可以算 median
            # 先根据 i,j 求 left,right
            left_max = nums2[j - 1] if i == 0 else nums1[i - 1] if j == 0 else max(nums1[i - 1], nums2[j - 1])
            if (m + n) % 2 == 1:  # 奇数时，左边最大值恰为 median
                return left_max
            right_min = nums2[j] if i == m else nums1[i] if j == n else min(nums1[i], nums2[j])
            return (left_max + right_min) / 2


print(findMedianSortedArrays([1, 3], [2]))
print(findMedianSortedArrays([1, 2], [3, 4]))
print(findMedianSortedArrays([4, 5], [1, 2, 3]))
