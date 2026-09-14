class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        vowels = "aeiou"
        order = {v: i for i, v in enumerate(vowels)}
        
        max_len = 0
        start = 0
        distinct = 1  # count of distinct vowels in current window
        
        for i in range(1, len(word)):
            prev, curr = word[i-1], word[i]
            if curr == prev:
                pass  # same vowel, window continues, distinct unchanged
            elif order[curr] == order[prev] + 1:
                distinct += 1
            else:
                # order broken, reset window
                start = i
                distinct = 1
            
            if distinct == 5:
                max_len = max(max_len, i - start + 1)
        
        return max_len