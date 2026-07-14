import math
from typing import List

class Solution:
    def subsequencePairCount(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        maxVal = max(nums)
        
        # Precompute gcd table for speed: gcd_table[a][b] = gcd(a, b)
        # a ranges over 0..maxVal (0 means "empty subsequence"), b ranges over actual nums values (1..maxVal)
        gcd_table = [[0] * (maxVal + 1) for _ in range(maxVal + 1)]
        for a in range(maxVal + 1):
            for b in range(maxVal + 1):
                gcd_table[a][b] = math.gcd(a, b)
        
        # dp[g1][g2] = number of ways to have processed elements so far such that
        # gcd of seq1's elements (or 0 if empty) = g1, gcd of seq2's elements (or 0 if empty) = g2
        dp = [[0] * (maxVal + 1) for _ in range(maxVal + 1)]
        dp[0][0] = 1
        
        for num in nums:
            new_dp = [row[:] for row in dp]  # case: skip this element (add to neither)
            
            for g1 in range(maxVal + 1):
                row = dp[g1]
                for g2 in range(maxVal + 1):
                    cnt = row[g2]
                    if cnt == 0:
                        continue
                    
                    # add num to seq1
                    ng1 = gcd_table[g1][num]
                    new_dp[ng1][g2] = (new_dp[ng1][g2] + cnt) % MOD
                    
                    # add num to seq2
                    ng2 = gcd_table[g2][num]
                    new_dp[g1][ng2] = (new_dp[g1][ng2] + cnt) % MOD
            
            dp = new_dp
        
        # Sum up all states where g1 == g2 and both are non-zero (non-empty subsequences)
        ans = 0
        for g in range(1, maxVal + 1):
            ans = (ans + dp[g][g]) % MOD
        
        return ans