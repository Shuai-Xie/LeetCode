import numpy as np


def draw_balls(times=0):
    ball_list = []
    while times > 0:
        color_id = np.random.choice([0, 1], p=ball_P)
        ball_list.append(ball_name[color_id])
        times -= 1
    return ball_list


ball_name = {
    0: '红',
    1: '白'
}
# 根据 B 设置 box
box1 = [0, 0, 0, 0, 0, 1, 1, 1, 1, 1]  # 5,5
box2 = [0, 0, 0, 1, 1, 1, 1, 1, 1, 1]  # 3,7
box3 = [0, 0, 0, 0, 0, 0, 1, 1, 1, 1]  # 6,4
box4 = [0, 0, 0, 0, 0, 0, 0, 0, 1, 1]  # 8,2

# Markov draw
# 初始概率分布
pi = np.array([0.25, 0.25, 0.25, 0.25]).T  # 4,1

# 状态转移矩阵 a_ij
A = np.array([
    [0, 1, 0, 0],  # 不同盒子选择下一个盒子的概率
    [0.4, 0, 0.6, 0],
    [0, 0.4, 0, 0.6],
    [0, 0, 0.5, 0.5]
])
for i in range(len(A)):
    print(f'box {i}:', np.mean(A[:, i]))

# 观测概率分布 b_j(k)
B = np.array([
    [0.5, 0.5],  # 不同盒子抓到 红/白球的概率
    [0.3, 0.7],
    [0.6, 0.4],
    [0.8, 0.2]
])

print('R:', np.mean(B[:, 0]))  # 0.55
print('W:', np.mean(B[:, 1]))  # 0.45


def chain_probs(pi, len=10):
    state_P = pi
    i = 1
    while i <= len:
        state_P = A @ state_P  # 当前 A，state_P 恒 = pi，相当于处于各个 box 的概率 始终不变
        ball_P = state_P @ B
        print(i)
        print(state_P)
        print(ball_P)
        i += 1


chain_probs(pi)
