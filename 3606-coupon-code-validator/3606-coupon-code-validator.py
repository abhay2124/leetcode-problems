class Solution:
    def validateCoupons(self, code, businessLine, isActive):
        order = {"electronics": 0, "grocery": 1, "pharmacy": 2, "restaurant": 3}
        valid = []
        
        for c, b, active in zip(code, businessLine, isActive):
            if active and b in order and c and all(ch.isalnum() or ch == '_' for ch in c):
                valid.append((order[b], c))
        
        valid.sort()
        return [c for _, c in valid]