from collections import defaultdict
from typing import List

class Solution:
    def longestEqualSubarray(self, nums: List[int], k: int) -> int:
        pos = defaultdict(list)
        for i, x in enumerate(nums):
            pos[x].append(i)
        
        ans = 0
        for p in pos.values():
            l = 0
            for r in range(len(p)):
                while (p[r] - p[l] + 1) - (r - l + 1) > k:
                    l += 1
                ans = max(ans, r - l + 1)
        
        return ans