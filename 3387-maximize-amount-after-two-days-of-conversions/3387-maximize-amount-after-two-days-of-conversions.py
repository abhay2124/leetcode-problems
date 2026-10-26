from collections import defaultdict
from typing import List

class Solution:
    def maxAmount(self, initialCurrency: str, pairs1: List[List[str]], rates1: List[float],
                  pairs2: List[List[str]], rates2: List[float]) -> float:
        
        def build(pairs, rates):
            g = defaultdict(list)
            for (a, b), r in zip(pairs, rates):
                g[a].append((b, r))
                g[b].append((a, 1.0 / r))
            return g
        
        def reach(g, start):
            # amount of each currency reachable from `start` holding 1.0 of start
            res = {start: 1.0}
            stack = [start]
            while stack:
                cur = stack.pop()
                for nxt, r in g[cur]:
                    if nxt not in res:
                        res[nxt] = res[cur] * r
                        stack.append(nxt)
            return res
        
        g1 = build(pairs1, rates1)
        g2 = build(pairs2, rates2)
        
        day1 = reach(g1, initialCurrency)       # 1 initial -> day1[c] of c
        day2 = reach(g2, initialCurrency)       # 1 initial -> day2[c] of c
        
        ans = 1.0
        for c, amt in day1.items():
            if c in day2:
                # converting c back to initial on day 2 gives amt / day2[c]
                ans = max(ans, amt / day2[c])
        
        return ans