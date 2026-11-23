from itertools import combinations
from typing import List

def _is_good(x: int) -> bool:
    d = list(map(int, str(x)))
    if len(d) == 1:
        return True
    inc = all(d[i] < d[i + 1] for i in range(len(d) - 1))
    dec = all(d[i] > d[i + 1] for i in range(len(d) - 1))
    return inc or dec

_GOOD = []
for size in range(1, 10):
    for c in combinations(range(1, 10), size):
        _GOOD.append(int("".join(map(str, c))))          # increasing
for size in range(2, 11):
    for c in combinations(range(10), size):
        _GOOD.append(int("".join(map(str, sorted(c, reverse=True)))))  # decreasing
_GOOD.sort()

_S = {s for s in range(0, 140) if _is_good(s)}

_MAXS = 150
_ways = [[0] * _MAXS for _ in range(17)]
_ways[0][0] = 1
for k in range(1, 17):
    for s in range(_MAXS):
        t = 0
        for d in range(10):
            if s - d >= 0:
                t += _ways[k - 1][s - d]
        _ways[k][s] = t


class Solution:
    def countFancy(self, l: int, r: int) -> int:
        def count_sum_good(N: int) -> int:
            digs = list(map(int, str(N)))
            n = len(digs)
            total = 0
            prefix = 0
            for i, dg in enumerate(digs):
                rem = n - i - 1
                for d in range(dg):
                    base = prefix + d
                    for s in _S:
                        t = s - base
                        if 0 <= t < _MAXS:
                            total += _ways[rem][t]
                prefix += dg
            if prefix in _S:
                total += 1          # N itself
            if 0 in _S:
                total -= 1          # remove the number 0
            return total

        def fancy(N: int) -> int:
            if N <= 0:
                return 0
            good = both = 0
            for g in _GOOD:
                if g > N:
                    break
                good += 1
                if sum(map(int, str(g))) in _S:
                    both += 1
            return good + count_sum_good(N) - both

        return fancy(r) - fancy(l - 1)