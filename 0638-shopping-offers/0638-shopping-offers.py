from functools import lru_cache
from typing import List

class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        n = len(price)
        
        # Drop offers that are never cheaper than buying items individually
        special = [s for s in special if s[-1] < sum(s[j] * price[j] for j in range(n))]
        
        @lru_cache(maxsize=None)
        def dfs(state):
            # Baseline: buy everything at regular price
            best = sum(state[j] * price[j] for j in range(n))
            
            for offer in special:
                nxt = []
                for j in range(n):
                    if offer[j] > state[j]:
                        break
                    nxt.append(state[j] - offer[j])
                else:
                    best = min(best, offer[-1] + dfs(tuple(nxt)))
            
            return best
        
        return dfs(tuple(needs))