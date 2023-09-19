import asyncio
from typing import List


async def is_rotate_str(a: str, b: str) -> bool:
    """
    旋转串 a 把第一个字符移到最后 得到 b  那么 b是a的旋转串, 一个字符的旋转串的旋转串也是它的旋转串
    判断a和b是否互为旋转串
    :param a:
    :param b:
    :return:
    """
    if len(a) != len(b):
        return False
    if a == b:
        return True
    for i in range(len(a)):
        if a[i:] + a[:i] == b:
            return True
    return False


async def solution(strs: List[str]) -> str:
    """
    判断 strs中是否有两个字符串匹配
    匹配的意思是 A和B互为旋转串
    :param strs:
    :return:
    """
    for i in range(len(strs)):
        for j in range(i + 1, len(strs)):
            if is_rotate_str(strs[i], strs[j]):
                return "YES"
    return "NO"


async def main():
    num_input = int(input())
    for _ in range(num_input):
        n = int(input())
        str_list: List[str] = ["" for _ in range(n)]
        for i in range(n):
            str_list[i] = input()
        print(solution(str_list))


if __name__ == "__main__":
    asyncio.run(main())