from typing import List


def solution(a: List[int], b: List[int]) -> List:
    # 对 nums_a 求中位数 nums_a[i] -> i
    # 根据nums_b的顺序删除a中对应下标的元素 a[b[i]]
    # 然后区域a中剩下数字的中位数 并记录
    def get_mid():
        _a = sorted(a)
        if len(_a) % 2 == 0:
            mid = (_a[len(_a) // 2] + _a[len(_a) // 2 - 1]) / 2.0
        else:
            mid = _a[len(_a) // 2]
        return mid

    ans = []
    cnt = 0
    while len(a) != 1:
        mid = get_mid()
        # mid如果是小数 则保留一位
        if mid % 1 != 0:
            mid = round(mid, 1)
        ans.append(mid)
        remove_idx = b[cnt]
        # print(f"mid:{mid} a[b[{cnt}]]=a[{remove_idx}]={a[remove_idx - 1]}")
        a.pop(remove_idx - 1)
        cnt += 1
    return ans


if __name__ == '__main__':
    num_input = int(input())
    input_pairs = []
    for i in range(num_input):
        _ = input()
        nums_a = list(map(int, input().split()))
        nums_b = list(map(int, input().split()))
        input_pairs.append((nums_a, nums_b))
    for nums_a, nums_b in input_pairs:
        ans = solution(nums_a, nums_b)
        print(" ".join(map(str, ans)))
    # print(solution([2, 2, 1, 3, 5], [3, 1, 2, 5]))
