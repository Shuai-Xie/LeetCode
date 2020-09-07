def has_same(circles):
    aa = circles
    aa.sort()
    for i in range(n - 1):
        if aa[i] == aa[i + 1]:  # 直接比较 arr
            return True
    return False


T = int(input())
res = []
for _ in range(T):
    n = int(input())
    circles = []
    for _ in range(n):
        circles.append(sorted(map(int, input().split())))
    if has_same(circles):
        res.append('YES')
    else:
        res.append('NO')

for v in res:
    print(v)
