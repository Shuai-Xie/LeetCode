n = 5
arr = [30, 60, 5, 15, 30]
# arr = [30, 60, 5, 15, 30, 10, 5]
state = [0 for _ in range(len(arr))]

ans = 0


def dfs(i):
    if i >= len(arr):
        return
    global ans
    for s in range(3):
        state[i] = s
        s1 = sum([arr[j] for j in range(i + 1) if state[j] == 1])
        s2 = sum([arr[j] for j in range(i + 1) if state[j] == 2])
        if s1 == s2:
            ans = max(ans, s1)
        dfs(i + 1)


dfs(0)
print(sum(arr) - 2 * ans)
