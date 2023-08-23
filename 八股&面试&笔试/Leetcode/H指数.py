from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        n = len(citations)
        # 从前往后遍历，如果当前的引用数大于等于剩余的论文数，那么就是H指数
        for i in range(n):
            if citations[i] >= n - i:
                return n - i
        return 0
