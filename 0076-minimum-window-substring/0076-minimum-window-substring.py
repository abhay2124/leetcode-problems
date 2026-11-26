from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = Counter(t)
        missing = len(t)
        best_l, best_len = 0, float('inf')
        left = 0

        for right, ch in enumerate(s):
            if need[ch] > 0:
                missing -= 1
            need[ch] -= 1

            if missing == 0:
                # shrink while the left char is surplus
                while need[s[left]] < 0:
                    need[s[left]] += 1
                    left += 1
                if right - left + 1 < best_len:
                    best_l, best_len = left, right - left + 1
                # drop the left char to look for the next window
                need[s[left]] += 1
                missing += 1
                left += 1

        return "" if best_len == float('inf') else s[best_l:best_l + best_len]