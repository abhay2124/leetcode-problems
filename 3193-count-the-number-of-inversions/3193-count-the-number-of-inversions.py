class Solution:
    def numberOfPermutations(self, n: int, requirements: List[List[int]]) -> int:
        MOD = 10**9 + 7
        MAXK = 400
        
        req = {}
        for e, c in requirements:
            req[e] = c
        
        # requirement at index 0 must have cnt == 0, otherwise impossible
        if 0 in req and req[0] != 0:
            return 0
        
        dp = [0] * (MAXK + 1)
        dp[0] = 1
        
        for length in range(1, n + 1):
            i = length - 1  # max delta possible when inserting the (length)-th element
            
            # prefix sums of current dp
            prefix = [0] * (MAXK + 2)
            for k in range(MAXK + 1):
                prefix[k + 1] = (prefix[k] + dp[k]) % MOD
            
            new_dp = [0] * (MAXK + 1)
            for k in range(MAXK + 1):
                low = max(0, k - i)
                new_dp[k] = (prefix[k + 1] - prefix[low]) % MOD
            
            dp = new_dp
            
            idx = length - 1 
            if idx in req:
                c = req[idx]
                if c > MAXK:
                    return 0
                for k in range(MAXK + 1):
                    if k != c:
                        dp[k] = 0
        
        return sum(dp) % MOD