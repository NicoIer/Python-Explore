from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        for start in range(len(s2) - len(s1) + 1):
            if self.check(s1, s2[start:start + len(s1)]):
                return True
        return False

    def check(self, s1: str, s2: str):
        # 是否每个字符的数量相等
        for i in range(26):
            if s1.count(chr(i + ord('a'))) != s2.count(chr(i + ord('a'))):
                return False
        return True
