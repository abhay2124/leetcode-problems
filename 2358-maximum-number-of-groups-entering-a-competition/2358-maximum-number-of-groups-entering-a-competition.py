class Solution:
    def maximumGroups(self, grades: List[int]) -> int:
        n = len(grades)
        k = 0
        total = 0
        while total + (k + 1) <= n:
            k += 1
            total += k
        return k