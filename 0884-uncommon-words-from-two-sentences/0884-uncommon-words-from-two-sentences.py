from collections import Counter

class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        count = Counter((s1 + " " + s2).split())
        return [word for word, c in count.items() if c == 1]   