def cal_snf(val, nums):
    return sum([abs(val - i) for i in nums])


def get_median(*nums):
    nums = sorted(nums)  # return list
    LEN = len(nums)
    if LEN % 2 == 1:
        return nums[LEN // 2]
    else:
        med1, med2 = nums[LEN // 2 - 1], nums[LEN // 2]
        print('med:', med1, med2)
        print('snf:', cal_snf(med1, nums), cal_snf(med2, nums))
        if cal_snf(med1, nums) <= cal_snf(med2, nums):
            return med1
        else:
            return med2


print(get_median(88, 75, 97, 86))
