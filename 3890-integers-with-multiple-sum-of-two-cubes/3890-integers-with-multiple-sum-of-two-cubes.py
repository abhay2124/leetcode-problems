from collections import defaultdict
from typing import List

class Solution:
    def findGoodIntegers(self, n: int) -> List[int]:
        count = defaultdict(int)
        a = 1
        while 2 * a ** 3 <= n:
            b = a
            while a ** 3 + b ** 3 <= n:
                count[a ** 3 + b ** 3] += 1
                b += 1
            a += 1
        
        return sorted(x for x, c in count.items() if c >= 2)