from typing import List


def solution(nums: List[int], k: int) -> int:
    """
     k 次操作 每次任意选一个数ai
     如果ai是偶数 则*2+1 如果ai是奇数 则*2
     求k次操作后的最小值
    :param nums:
    :param k:
    :return:
    """
    for _ in range(k):
        nums.sort()
        nums[0] <<= 1
    return sum(nums)


if __name__ == "__main__":
    n, k = map(int, input().split())
    nums = list(map(int, input().split()))
    print(solution(nums, k))
