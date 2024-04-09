class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        con = set()
        for k in nums:
            for i in range(2, int(math.sqrt(k))+1):
                while k % i == 0:
                    con.add(i)
                    k //= i
            if k > 1:
                con.add(k)
        return len(con)



        