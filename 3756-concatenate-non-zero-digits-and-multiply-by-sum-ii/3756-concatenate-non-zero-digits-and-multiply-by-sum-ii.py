class Solution:
    def sumAndMultiply(self, s, queries):
        MOD = 10**9 + 7
        m = len(s)
        
        prefix_x   = [0] * (m + 1)
        prefix_sum = [0] * (m + 1)
        prefix_cnt = [0] * (m + 1)
        
        for i in range(m):
            d = int(s[i])
            if d != 0:
                prefix_x[i+1]   = (prefix_x[i] * 10 + d) % MOD
                prefix_sum[i+1] = prefix_sum[i] + d
                prefix_cnt[i+1] = prefix_cnt[i] + 1
            else:
                prefix_x[i+1]   = prefix_x[i]
                prefix_sum[i+1] = prefix_sum[i]
                prefix_cnt[i+1] = prefix_cnt[i]
        
        answer = []
        for l, r in queries:
            cnt  = prefix_cnt[r+1] - prefix_cnt[l]
            x    = (prefix_x[r+1] - prefix_x[l] * pow(10, cnt, MOD)) % MOD
            dsum = prefix_sum[r+1] - prefix_sum[l]
            answer.append((x * dsum) % MOD)
        
        return answer