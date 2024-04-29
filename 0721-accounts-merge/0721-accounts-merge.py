class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        self.p = {i:i for i in range(len(accounts))}
               
        eta = dict()
        for i, acc in enumerate(accounts):
            for email in acc[1:]:
                if email in eta:
                    self.union(eta[email], i)
                    continue
                
                eta[email] = i
    
        ate = dict()
        for email in eta:
            acc = self.find(eta[email])
            
            if acc in ate:
                ate[acc].append(email)
            else:
                ate[acc] = [email]
             
        res = []   
        for p in ate:
            res.append([accounts[p][0]] + sorted(ate[p]))
            
        return res
    
    def union(self, a, b):
        self.p[self.find(b)] = self.find(a)

    def find(self, res):
        while self.p[res] != res:
            self.p[res] = self.p[self.p[res]]
            res = self.p[res]

        return res