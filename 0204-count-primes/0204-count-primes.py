class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2:
            return 0
        i = 2
        primes = set()
        for i in range(2, int(math.sqrt(n))+1):
            if i not in primes:
                for j in range(i*i, n, i):
                    primes.add(j)
        return n - 2 - len(primes)