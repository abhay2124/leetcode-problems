import heapq
from typing import List

class Solution:
    def maxEarnings(self, meetings: List[List[int]]) -> int:
        meetings.sort()  # by start time
        heap = []        # (end, g)
        best = float('-inf')
        ans = float('-inf')
        
        for s, e, r in meetings:
            while heap and heap[0][0] <= s:
                _, g = heapq.heappop(heap)
                if g > best:
                    best = g
            
            h = r
            if best != float('-inf'):
                h = max(h, best + r + s)
            
            ans = max(ans, h)
            heapq.heappush(heap, (e, h - e))
        
        return ans