from typing import List


def solution(nums: List[int]):
    """
    :param nums: 数组
    :return: nums最多能组成几对长度为5的顺子
    """
    nums.sort()
    ans = 0

    start = nums[0]  # 默认起点
    max_end = nums[-1]  # 默认终点
    while max_end - start + 1 >= 5 and len(nums) >= 5:  # 从start开始，找到连续的5个数
        start = nums[0]
        max_end = nums[-1]
        if start in nums and start + 1 in nums and start + 2 in nums and start + 3 in nums and start + 4 in nums:
            ans += 1
            nums.remove(start)
            nums.remove(start + 1)
            nums.remove(start + 2)
            nums.remove(start + 3)
            nums.remove(start + 4)
        else:
            nums.pop(0)
    return ans


if __name__ == "__main__":
    print(solution([
        1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 7, 8, 9, 10
    ]))
