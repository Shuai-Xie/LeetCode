class Solution:
    def get_cols(self, n, numRows):
        step = 2 * numRows - 2  # 一个单元的长度
        base, remain = n // step, n % step
        cols = base * (1 + numRows - 2)
        if 0 < remain <= numRows:  # 多出首列
            cols += 1
        elif remain > numRows:  # 多出后面的列
            cols += (1 + remain - numRows)
        return cols

    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        n = len(s)
        step = 2 * numRows - 2  # 步长, 首行
        res = ''

        for i in range(numRows):
            if i < n:
                res += s[i]
            idx = i  # row 首列, 即中间行分两步
            one_step = step - i * 2  # 4
            two_step = step - one_step  # 0

            if one_step == step or two_step == step:  # 首行/末行
                idx += step
                while idx < n:
                    res += s[idx]
                    idx += step
            else:  # 中间行
                while True:
                    idx += one_step
                    if idx < n:
                        res += s[idx]
                    else:
                        break
                    idx += two_step
                    if idx < n:
                        res += s[idx]
                    else:
                        break

        return res


solver = Solution()
s = 'LEETCODEISHIRING'
print(solver.convert(s, 1))
print(solver.convert(s, 2))
print(solver.convert(s, 3))
print(solver.convert(s, 4))
