class Solution:
    def findPrimePairs(self, n: int) -> List[List[int]]:
        is_prime = [True for i in range(n+1)]
        is_prime[0] = is_prime[1] = False
        i = 2
        while i*i <= n:
            if is_prime[i]:
                j = i*i
                while j <= n:
                    is_prime[j] = False
                    j += i
            i += 1
        dicti = {ind: val for ind,val in enumerate(is_prime)}
        sol_arr = []
        for k in range(2, (n//2)+1):
            if dicti[k] and dicti[n-k]:
                sol_arr.append([k, n-k])
        return sol_arr
        