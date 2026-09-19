from typing import List

class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0

        prev = [-1] * n
        last = {}
        for i, v in enumerate(nums):
            if v in last:
                prev[i] = last[v]
            last[v] = i

        c = [1 if v % 2 == 0 else -1 for v in nums]

        size = 4 * n
        min_val = [0] * size
        max_val = [0] * size
        lazy = [0] * size

        def push_down(node):
            if lazy[node]:
                for child in (2 * node, 2 * node + 1):
                    min_val[child] += lazy[node]
                    max_val[child] += lazy[node]
                    lazy[child] += lazy[node]
                lazy[node] = 0

        def update(node, l, r, ql, qr, val):
            if qr < l or r < ql:
                return
            if ql <= l and r <= qr:
                min_val[node] += val
                max_val[node] += val
                lazy[node] += val
                return
            push_down(node)
            mid = (l + r) // 2
            update(2 * node, l, mid, ql, qr, val)
            update(2 * node + 1, mid + 1, r, ql, qr, val)
            min_val[node] = min(min_val[2 * node], min_val[2 * node + 1])
            max_val[node] = max(max_val[2 * node], max_val[2 * node + 1])

        def query(node, l, r, ql, qr):
            if qr < l or r < ql or ql > qr:
                return -1
            if not (min_val[node] <= 0 <= max_val[node]):
                return -1
            if l == r:
                return l
            push_down(node)
            mid = (l + r) // 2
            res = -1
            if ql <= mid:
                res = query(2 * node, l, mid, ql, qr)
            if res != -1:
                return res
            if qr > mid:
                res = query(2 * node + 1, mid + 1, r, ql, qr)
            return res

        ans = 0
        for r in range(n):
            p = prev[r]
            update(1, 0, n - 1, p + 1, r, c[r])
            l = query(1, 0, n - 1, 0, r)
            if l != -1:
                ans = max(ans, r - l + 1)

        return ans