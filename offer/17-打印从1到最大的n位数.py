from typing import List


class Solution:
    def printNumbers(self, n: int) -> List[int]:
        # 从1到最大的 n 位 10进制
        return list(range(1, 10 ** n))


s = Solution()
s.printNumbers(2)
