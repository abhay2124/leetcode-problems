class Solution:
    def getLucky(self, s: str, k: int) -> int:
        digits = ''.join(str(ord(c) - 96) for c in s)
        num = sum(int(d) for d in digits)  # transform #1
        for _ in range(k - 1):
            num = sum(int(d) for d in str(num))
        return num
        