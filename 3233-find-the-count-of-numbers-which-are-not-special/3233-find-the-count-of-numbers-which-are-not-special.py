class Solution:
    def nonSpecialCount(self, l: int, r: int) -> int:
        hi = math.isqrt(r)          # floor(sqrt(r))
        lo = math.isqrt(l - 1) + 1  # ceil(sqrt(l))
        
        # Sieve of Eratosthenes up to hi
        is_prime = [True] * (hi + 1)
        if hi >= 0:
            is_prime[0] = False
        if hi >= 1:
            is_prime[1] = False
        for i in range(2, math.isqrt(hi) + 1):
            if is_prime[i]:
                for j in range(i*i, hi + 1, i):
                    is_prime[j] = False
        
        special_count = sum(1 for p in range(lo, hi + 1) if is_prime[p])
        
        return (r - l + 1) - special_count