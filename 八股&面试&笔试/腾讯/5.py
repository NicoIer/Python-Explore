from typing import List


def solution(nums: List[int], k: int) -> int:
    # 每次可以将nums中的一个数的二进制位的第一位变成0
    # 求k次后 sum(nums) 的最小值
    # 1111(15) -> 0111(7)
    nums.sort(reverse=True)
    for i in range(k):
        # print(nums)
        # print(f"{nums[0]}-->{nums[0] & (nums[0] - 1)}")# 把第一位变成0
        nums[0] &= (nums[0] - 1)
        nums.sort(reverse=True)

    return sum(nums)


if __name__ == '__main__':
    print(solution([9, 6], 2))
    _, k = map(int, input().split())
    nums = list(map(int, input().split()))
    print(solution(nums, k))
