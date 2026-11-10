class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        def count_steps(prefix: int) -> int:
            steps = 0
            lo, hi = prefix, prefix
            while lo <= n:
                steps += min(n + 1, hi + 1) - lo
                lo *= 10
                hi = hi * 10 + 9
            return steps

        cur = 1
        k -= 1
        while k > 0:
            steps = count_steps(cur)
            if steps <= k:
                cur += 1
                k -= steps
            else:
                cur *= 10
                k -= 1
        return cur