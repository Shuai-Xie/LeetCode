num_ji, total_mo, total_times = map(int, input().split())

inputs = []

for _ in range(num_ji):  # n 个技能
    atk, mo, time = map(int, input().split())
    inputs.append([atk, mo, time])

"""
3个约束条件
1. 技能 mo <= 角色 mo
2. 技能未冷却
3. 技能伤害 为当前三者最大
"""

D = [0]
cold_records = [0] * num_ji
for i in range(1, time_live + 1):
    # 当前技能的上一步 只能是 所有技能中的某个
    cands = [(j, attacks[j], mos[j], colds[j]) for j in range(num_ji) if cold_records[j] % colds[j] == 0 and mos[j] <= total_mo]
