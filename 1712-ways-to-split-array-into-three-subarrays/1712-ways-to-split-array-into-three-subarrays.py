class Solution:
    def waysToSplit(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]
        
        total = prefix[n]
        count = 0
        lo = hi = 0
        
        for i in range(1, n - 1):
            if lo < i + 1:
                lo = i + 1
            while lo <= n - 1 and prefix[lo] < 2 * prefix[i]:
                lo += 1
            
            if hi < i + 1:
                hi = i + 1
            while hi <= n - 1 and 2 * prefix[hi] <= total + prefix[i]:
                hi += 1
          
            valid_hi = hi - 1
            if lo <= valid_hi and lo <= n - 1:
                count = (count + (valid_hi - lo + 1)) % MOD
        
        return count