from typing import List


def solution(nums: List[int]) -> int:
    x = 0
    # 任意选择怪兽战斗 如果 x < a[i] 则 x = a[i] 勇气值提升 a[i] - x
    # 如果 x >= a[i] 则 x = a[i] 勇气值降低 x - a[i]
    # 求累计提升的勇气值的最大值
    # 波浪形的数组可以得到最大值 0 2 1 2 => 3
    nums.append(0)
    nums.sort()
    # 把nums变成波浪形数组
    for i in range(1, len(nums) - 1, 2):
        nums[i], nums[i + 1] = nums[i + 1], nums[i]
    # print(nums)
    for i in range(1, len(nums)):
        if nums[i] > nums[i - 1]:
            x += nums[i] - nums[i - 1]
    return x


if __name__ == '__main__':
    print(solution([7,2,8,1]))
    _ = input()
    nums = list(map(int, input().split()))
    print(solution(nums))
