class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        n = len(s)
        for c in t:
            if i < n and s[i] == c:
                i += 1
        return i == n