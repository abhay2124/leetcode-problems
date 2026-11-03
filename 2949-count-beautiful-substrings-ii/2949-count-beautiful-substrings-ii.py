from collections import defaultdict

class Solution:
    def beautifulSubstrings(self, s: str, k: int) -> int:
        # L = product of p^ceil(e/2) over prime factorization of k
        L = 1
        x = k
        p = 2
        while p * p <= x:
            if x % p == 0:
                e = 0
                while x % p == 0:
                    x //= p
                    e += 1
                L *= p ** ((e + 1) // 2)
            p += 1
        if x > 1:
            L *= x  # exponent 1 -> ceil(1/2) = 1
        
        mod = 2 * L
        vowels = set("aeiou")
        
        cnt = defaultdict(int)
        cnt[(0, 0)] = 1  # empty prefix at index 0
        bal = 0
        ans = 0
        
        for idx, ch in enumerate(s, 1):
            bal += 1 if ch in vowels else -1
            key = (bal, idx % mod)
            ans += cnt[key]
            cnt[key] += 1
        
        return ans