from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        for num in nums:
            for i in range(len(ans)):
                ans.append(ans[i] + [num])
            ans.append([num])
        ans.append([])
        return ans
