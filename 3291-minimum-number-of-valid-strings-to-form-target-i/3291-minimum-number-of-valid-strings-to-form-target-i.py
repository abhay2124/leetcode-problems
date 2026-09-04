class Solution:
    def minValidStrings(self, words: list[str], target: str) -> int:
        # Build trie
        root = {}
        for w in words:
            node = root
            for c in w:
                node = node.setdefault(c, {})

        n = len(target)
        reach = [0] * n

        for i in range(n):
            node = root
            j = i
            while j < n and target[j] in node:
                node = node[target[j]]
                j += 1
            reach[i] = j  
        jumps = 0
        curEnd = 0
        farthest = 0

        for i in range(n):
            if i > curEnd:
                return -1
            farthest = max(farthest, reach[i])
            if i == curEnd:
                if farthest == curEnd:
                    return -1  # stuck, no progress possible
                jumps += 1
                curEnd = farthest

        return jumps if curEnd >= n else -1