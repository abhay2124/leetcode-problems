from typing import List

class Solution:
    def totalStrength(self, strength: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(strength)

        # P[k] = sum of first k elements, PP[k] = P[0] + ... + P[k-1]
        P = [0] * (n + 1)
        for i in range(n):
            P[i + 1] = P[i] + strength[i]
        PP = [0] * (n + 2)
        for k in range(n + 1):
            PP[k + 1] = PP[k] + P[k]

        left = [-1] * n   # previous strictly smaller
        right = [n] * n   # next smaller or equal
        stack = []
        for i in range(n):
            while stack and strength[stack[-1]] >= strength[i]:
                right[stack.pop()] = i
            left[i] = stack[-1] if stack else -1
            stack.append(i)

        ans = 0
        for i in range(n):
            L, R = left[i], right[i]
            right_sum = PP[R + 1] - PP[i + 1]
            left_sum = PP[i + 1] - PP[L + 1]
            total = (i - L) * right_sum - (R - i) * left_sum
            ans = (ans + strength[i] * (total % MOD)) % MOD

        return ans