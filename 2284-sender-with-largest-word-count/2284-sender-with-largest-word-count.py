from collections import defaultdict

class Solution:
    def largestWordCount(self, messages: List[str], senders: List[str]) -> str:
        count = defaultdict(int)
        for msg, sender in zip(messages, senders):
            count[sender] += len(msg.split())
        
        return max(count.items(), key=lambda x: (x[1], x[0]))[0]