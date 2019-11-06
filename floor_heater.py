import itertools


def print_each_P_floors(floors, heater_floors):
    if len(heater_floors) > 0:
        total_steps = 0
        print('floor  heater  steps')
        for p in range(1, floors + 1):
            cand_steps = [abs(p - h) for h in heater_floors]
            min_idx = cand_steps.index(min(cand_steps))  # min steps
            if p > heater_floors[min_idx]:  # 下楼
                print('{:^5d}  {:^6d}  {:^5d}'.format(p, heater_floors[min_idx], -cand_steps[min_idx]))
            else:  # 上楼
                print('{:^5d}  {:^6d}  {:^5d}'.format(p, heater_floors[min_idx], cand_steps[min_idx]))
            total_steps += cand_steps[min_idx]
        print('total steps:', total_steps)
    else:
        print('no solution!')


def best_heater_floors(floors, heaters):
    """
    热水器放置问题 两个约束条件
      1.每层楼的人 打热水 上下楼层最少
      2.热水器放置的 总楼层数之和最小 成本最小
    选择时，在能满足 1 的情况下满足 2，先按 1 排序 再按 2
    :param floors: 楼层总数
    :param heaters: 热水器数量
    :return: heater_floors 热水器放置的楼层
    """
    # 可能的放置情况，从中选取
    cand_heater_floors = list(itertools.combinations(range(1, floors + 1), heaters))
    total_step_floors = []  # idx corresponds to idx in cand_heater_floors
    for heater_floors in cand_heater_floors:
        # each heaters
        total_steps = 0  # sum of min_step of each person
        total_floors = sum(heater_floors)
        for p in range(1, floors + 1):  # 1-5
            # each person's floor - each heater's floor
            min_step = min([abs(p - h) for h in heater_floors])
            total_steps += min_step
        total_step_floors.append((total_steps, total_floors))

    # 双成本最小的
    heater_floors = cand_heater_floors[total_step_floors.index(min(total_step_floors))]
    return heater_floors


def nearest_divided_number(a, b):
    assert a > b
    q, r = a // b, a % b  # 商，余数
    if r >= b / 2:  # 余数 >= 除数/2
        return a + b - r
    else:
        return a - r


def mid_val(a):
    if a % 2 == 0:
        return a // 2
    else:
        return a // 2 + 1


def better_heater_floors(floors, heaters):
    """
    划分成 楼层子区间 考虑
    :param floors:
    :param heaters:
    :return:
    """
    heater_floors = []

    nearest = nearest_divided_number(floors, heaters)
    sub_floors = nearest // heaters
    remainder = floors - sub_floors * (heaters - 1)  # 不整除的放到1个区间
    mid_rem, mid_sub = mid_val(remainder), mid_val(sub_floors)

    # 往下/往上 分配问题
    if nearest > floors:  # 上整下补
        heater_floors.append(mid_rem)  # 第1个
        for idx in range(1, heaters):  # 后 heaters - 1 个
            heater_floors.append(remainder + mid_sub + (idx - 1) * sub_floors)
    else:  # 上补下整
        for idx in range(heaters - 1):  # 前 heaters - 1 个
            heater_floors.append(mid_sub + idx * sub_floors)
        heater_floors.append(sub_floors * (heaters - 1) + mid_rem)  # 最后1个

    return heater_floors


import time


def test_func(floors=5, heaters=2):
    print('floors, heaters:', floors, heaters)
    st = time.process_time_ns()
    heater_floors = best_heater_floors(floors, heaters)
    print('result:', heater_floors)
    print('time:', time.process_time_ns() - st)
    # print_each_P_floors(floors, heater_floors)

    st = time.process_time_ns()
    heater_floors = better_heater_floors(floors, heaters)
    print('result:', heater_floors)
    print('time:', time.process_time_ns() - st)
    # print_each_P_floors(floors, heater_floors)


if __name__ == '__main__':
    test_func(5, 2)
    test_func(8, 2)
    test_func(10, 3)
    test_func(19, 2)
    test_func(50, 3)
