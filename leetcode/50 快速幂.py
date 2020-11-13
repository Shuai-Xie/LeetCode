"""
递归：O(log(n)) + O(log(n)) 栈空间
1.分段思想，每个子段已经计算过，直接将结果相乘
2.可将原始 n 段相乘，分为任意子段个数
3.递归树的构建过程中，并没出现子问题重叠，q 不断以指数速度减少，堆栈计算，自小到大，没有重复

分治将子问题的解，乘方处理，自上而下递归 比较好判断 当前子问题 是直接乘方，还是需要多乘 x
迭代怎么做？

迭代
1.转化为 二进制的乘数累加，乘方项表示为 二进制形式，然后从右向左，不断逢1相乘

"""


class Solution:
    def myPow(self, x: float, n: int) -> float:
        def quickPow(n):
            # 使用递归法，分治使用之前运算的结果
            if n == 0:  # 递归出口，0次幂 = 1
                return 1
            y = quickPow(n // 2)  # y*y 更好? y**2 报错; 递归回来再向后计算，不存在重复运算
            return y * y if n % 2 == 0 else y * y * x

        return quickPow(n) if n >= 0 else 1 / quickPow(-n)

    def myPow3(self, x: float, n: int) -> float:
        # 同样递归思想，将分治次数变为 O(log_3(n))
        def quickPow(n):
            if n == 0:  # 递归出口，0次幂 = 1
                return 1
            q, r = n // 3, n % 3
            y = quickPow(q)
            if r == 0:  # 可被整除
                return y * y * y
            elif r == 1:
                return y * y * y * x
            else:
                return y * y * y * x * x

        return quickPow(n) if n >= 0 else 1 / quickPow(-n)

    def myPow_iter(self, x: float, n: int) -> float:
        """
        二进制，左移 *2，右移 //2；取末尾二进制数 %2
        计算过程与迭代法不同，因为 ans 项每次的 乘数不同；
            迭代法 ans 的乘数始终为 2的幂
        """
        negative = True if n < 0 else False
        if negative:
            n = -n

        ans = 1
        mul_x = x
        while n > 0:
            if n % 2 == 1:  # 二进制最后1项
                ans *= mul_x
            mul_x *= mul_x  # 左移进位
            n //= 2  # 右移，去掉末位

        return 1 / ans if negative else ans


s = Solution()
print(s.myPow(2, -1000))
print(s.myPow3(2, -1000))

# print(s.myPow_iter(2, -2147483648))

# print(s.myPow3(2, 100))
# print(s.myPow_iter(2, 100))
