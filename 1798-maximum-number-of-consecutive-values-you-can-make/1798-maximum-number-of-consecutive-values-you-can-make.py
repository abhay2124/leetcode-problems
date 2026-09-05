class Solution:
    def getMaximumConsecutive(self, coins: list[int]) -> int:
        coins.sort()
        reach = 1  
        for c in coins:
            if c > reach:
                break
            reach += c
        return reach