from typing import List

class Solution:
    def countValidSubarrays(self, nums: List[int], x: int) -> int:
        n = len(nums)
        ch = str(x)
        count = 0
        for l in range(n):
            s = 0
            for r in range(l, n):
                s += nums[r]
                if s % 10 == x and str(s)[0] == ch:
                    count += 1
        return count