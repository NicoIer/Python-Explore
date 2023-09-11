"""
假设长度为n的二进制位串S
其k下的校验和为 所有长度为k的子串 的异或结果

cal(000111) = 00 ^ 00 ^ 01 ^ 11 ^ 11 = 01
"""


def solution(n: int, k: int) -> int:
    """
    :param n:
    :param k:
    :return: 多少个长度为n 且 与S不同的二进制位串 可以产生和S相同的校验和 (mod (10**9+7))
    """

    # 1. 生成所有长度为n的二进制位串
    # 2. 计算每个二进制位串的校验和
    # 3. 计算与S不同的二进制位串的校验和
    # 4. 返回结果

    def cal(bin_str: str, k: int) -> int:
        """
        计算二进制位串的校验和
        :param bin_str: 二进制位串
        :param k: 校验和的长度
        :return: 校验和
        """
        ans = 0
        for i in range(len(bin_str) - k + 1):
            ans ^= int(bin_str[i:i + k], 2)
        return ans

    # 1.
    all_bin_strs = []
    for i in range(2 ** n):
        all_bin_strs.append(bin(i)[2:].zfill(n))
    # 2.
    all_bin_strs_sum = []
    for bin_str in all_bin_strs:
        all_bin_strs_sum.append(cal(bin_str, k))
    # 3.
    S = all_bin_strs[0]
    S_sum = all_bin_strs_sum[0]
    diff_bin_strs_sum = []
    for i in range(1, len(all_bin_strs)):
        if all_bin_strs_sum[i] != S_sum:
            diff_bin_strs_sum.append(all_bin_strs_sum[i])
    # 4.
    return sum(diff_bin_strs_sum) % (10 ** 9 + 7)


if __name__ == '__main__':
    num_input = int(input())
    for i in range(num_input):
        n, k = map(int, input().split())
        print(solution(n, k))
