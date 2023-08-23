from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        idxMap = {}
        for i, num in enumerate(numbers):
            if target - num in idxMap:
                return [idxMap[target - num] + 1, i + 1]
            idxMap[num] = i
        return [-1, -1]