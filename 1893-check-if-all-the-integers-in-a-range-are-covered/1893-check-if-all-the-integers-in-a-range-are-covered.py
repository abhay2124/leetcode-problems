class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        covered = [False] * 51
        for start, end in ranges:
            for x in range(start, end + 1):
                covered[x] = True
        
        return all(covered[x] for x in range(left, right + 1))