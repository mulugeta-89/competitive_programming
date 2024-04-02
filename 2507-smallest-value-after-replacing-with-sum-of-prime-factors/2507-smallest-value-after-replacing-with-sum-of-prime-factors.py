class Solution:
    def smallestValue(self, n: int) -> int:
        if n == 4:
            return 4
        def finder(k):
            fac = []
            for i in range(2, int(math.sqrt(k))+1):
                while k % i == 0:
                    fac.append(i)
                    k //= i
            if k > 1:
                fac.append(k)
            return fac
        first = finder(n)
        while len(first) > 1:
            first = finder(sum(first))
        return first[0]
        