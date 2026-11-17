from typing import List

class Solution:
    def maxValidPairSum(self, nums: List[int], k: int) -> int:
        best = 0
        prefix_max = 0  # max of nums[0..j-k]
        for j in range(k, len(nums)):
            prefix_max = max(prefix_max, nums[j - k])
            best = max(best, prefix_max + nums[j])
        return best
        