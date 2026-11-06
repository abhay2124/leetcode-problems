from collections import Counter
from typing import List

class Solution:
    def partitionArray(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        if n % k != 0:
            return False
        g = n // k
        return max(Counter(nums).values()) <= g