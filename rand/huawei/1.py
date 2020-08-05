def lucky_name():
    score_dict = {chr(ord('A') + i): i + 1 for i in range(26)}  # 65-90
    score_dict.update({chr(ord('a') + i): i + 1 for i in range(26)})  # 97-122

    def get_luck(n):
        s = 0
        for c in n:
            s += score_dict[c]
        return s

    names = input().split()
    target = get_luck(names[0])

    scores = [(abs(get_luck(n) - target), -(idx + 1)) for idx, n in enumerate(names[1:])]
    scores.sort()  # 糟糕，还搞两个 双 id 排序...

    return names[abs(scores[0][1])]


def get_luck_name():
    def get_luck(n):
        luck = 0
        for c in n:
            s = ord(c) - ord('A') if 'A' <= c <= 'Z' else ord(c) - ord('a')  # 没必要+1，大家都少1
            luck += s
        return luck

    names = input().split()
    target = get_luck(names[0])

    # 不超过 10 位
    min_diff = float('inf')  # 没有专门表示整数的无穷大
    ans = 0
    for i in range(1, len(names)):
        diff = abs(get_luck(names[i]) - target)
        if diff <= min_diff:  # 顺序遍历，只要使用 <= 判断，就能拿到最后一个结果
            min_diff = diff
            ans = i

    return names[ans]


print(get_luck_name())
