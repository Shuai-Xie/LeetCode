class Solution:
    def replaceSpace(self, s: str) -> str:
        # return '%20'.join(s.split(' '))
        return s.replace(' ', '%20')

    def replaceSpace2(self, s: str) -> str:
        res = ''
        for c in s:
            if c == ' ':
                res += '%20'
            else:
                res += c
        return res


a = Solution()
s = "We are happy."
print(a.replaceSpace(s))
print(a.replaceSpace2(s))
