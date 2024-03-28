class Solution:
    def minimizeSet(self, divisor1: int, divisor2: int, uniqueCnt1: int, uniqueCnt2: int) -> int:
        l, r = 0, 1 << 32 - 1
        lcm = math.lcm(divisor1, divisor2)
        def checkValid(num):
            notDivisible1 = num - (num//divisor1)
            if notDivisible1 < uniqueCnt1:
                return False
            notDivisible2 = num - (num//divisor2)
            if notDivisible2 < uniqueCnt2:
                return False
            notDivisible3 = num - (num//lcm)
            if notDivisible3 < (uniqueCnt1 + uniqueCnt2):
                return False
            return True
        while l <= r:
            mid = (l+r)//2
            if checkValid(mid):
                r = mid - 1
            else:
                l = mid + 1
        return l