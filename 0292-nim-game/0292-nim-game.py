class Solution:
    def canWinNim(self, n: int) -> bool:
        if n % 2 != 0:
            return True
        if n % 2 == 0 and (n//2)%2 != 0:
            return True
        else:
            return False
        