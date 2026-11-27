class Solution:
    def distMoney(self, money: int, children: int) -> int:
        if money < children:
            return -1
        extra = money - children
        k = min(extra // 7, children)
        rem = extra - 7 * k
        if k == children and rem > 0:
            k -= 1
        elif k == children - 1 and rem == 3:
            k -= 1
        return k