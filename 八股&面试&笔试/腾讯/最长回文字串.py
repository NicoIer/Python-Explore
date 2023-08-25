def solution(s: str) -> str:
    """
    :param s: str
    :return: 最长回文字串
    """
    start, end = 0, len(s) - 1
    ans_start, ans_end = 0, 0
    for i in range(len(s)):
        for j in range(len(s) - 1, i, -1):
            start, end = i, j
            while start < end:
                if s[start] == s[end]:
                    start += 1
                    end -= 1
                else:
                    break
            if start >= end and j - i > ans_end - ans_start:
                ans_start, ans_end = i, j
    return s[ans_start:ans_end + 1]


if __name__ == "__main__":
    s = input()
    print(solution(s))
