class TrieNode:
    __slots__ = ('children', 'count')
    def __init__(self):
        self.children = {}
        self.count = 0

class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        root = TrieNode()
        
        # Build trie
        for word in words:
            node = root
            for ch in word:
                if ch not in node.children:
                    node.children[ch] = TrieNode()
                node = node.children[ch]
                node.count += 1
        
        # Query scores
        answer = []
        for word in words:
            node = root
            total = 0
            for ch in word:
                node = node.children[ch]
                total += node.count
            answer.append(total)
        
        return answer