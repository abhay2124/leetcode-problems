from collections import deque, defaultdict
from bisect import bisect_left, bisect_right
from typing import List

class Router:

    def __init__(self, memoryLimit: int):
        self.limit = memoryLimit
        self.queue = deque()
        self.seen = set()
        self.ts = defaultdict(list)    
        self.head = defaultdict(int)  

    def _remove_oldest(self):
        s, d, t = self.queue.popleft()
        self.seen.discard((s, d, t))
        self.head[d] += 1
        return [s, d, t]

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        key = (source, destination, timestamp)
        if key in self.seen:
            return False
        if len(self.queue) == self.limit:
            self._remove_oldest()
        self.queue.append(key)
        self.seen.add(key)
        self.ts[destination].append(timestamp)
        return True

    def forwardPacket(self) -> List[int]:
        if not self.queue:
            return []
        return self._remove_oldest()

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        arr = self.ts[destination]
        h = self.head[destination]
        lo = bisect_left(arr, startTime, h)
        hi = bisect_right(arr, endTime, h)
        return hi - lo