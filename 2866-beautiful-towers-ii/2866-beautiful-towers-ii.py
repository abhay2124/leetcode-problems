from typing import List

class Solution:
    def maximumSumOfHeights(self, maxHeights: List[int]) -> int:
        n = len(maxHeights)
        left = [0] * n
        right = [0] * n

        stack = []
        for i in range(n):
            while stack and maxHeights[stack[-1]] >= maxHeights[i]:
                stack.pop()
            p = stack[-1] if stack else -1
            left[i] = (left[p] if p >= 0 else 0) + maxHeights[i] * (i - p)
            stack.append(i)

        stack = []
        for i in range(n - 1, -1, -1):
            while stack and maxHeights[stack[-1]] >= maxHeights[i]:
                stack.pop()
            p = stack[-1] if stack else n
            right[i] = (right[p] if p < n else 0) + maxHeights[i] * (p - i)
            stack.append(i)

        return max(left[i] + right[i] - maxHeights[i] for i in range(n))