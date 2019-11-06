import itertools

m, n = 5, 2

# 排列数 A_n/m =  m! / (m-n)! = 20
A = list(itertools.permutations(range(1, m + 1), n))
print(len(A), A)

# 组合数 C_n/m = A_n/m / A_n/n = 20 / 2 = 10
# 除数 A_n/n 考虑了抽出 元组的可能顺序情况，n=2，2种情况，n=3，6种情况
C = list(itertools.combinations(range(1, m + 1), n))
print(len(C), C)

# 有放回组合，还可能抽到自身，15种结果 C_n/m + m
C2 = list(itertools.combinations_with_replacement(range(1, m + 1), n))
print(len(C2), C2)

# 交并补
print('并集')  # 使用 sorted 排序同时，转成 list
union_CC2 = sorted(set(C) | set(C2))  # union
print(len(union_CC2), union_CC2)

print('交集')
inter_CC2 = sorted(set(C) & set(C2))  # intersection
print(len(inter_CC2), inter_CC2)

print('差集')
diff_CC2 = sorted(set(C) ^ set(C2))
print(len(diff_CC2), diff_CC2)

print('补集')
print(set(C) - set(C2))  # difference
print(set(C2) - set(C))
