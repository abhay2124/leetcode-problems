class Solution:
    def sumAndMultiply(self, n):
        digits = [d for d in str(n) if d != '0']
        
        if not digits:
            x = 0
        else:
            x = int(''.join(digits))
        
        total = sum(int(d) for d in str(x))
        
        return x * total