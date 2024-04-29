class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        dicti = {i:i for i in ascii_lowercase}

        def parent(x):
            if x == dicti[x]:
                return x
            x = parent(dicti[x])
            return x
        def union(x, y):
            root_x = parent(x)
            root_y = parent(y)

            dicti[root_x] = dicti[root_y] = min(root_x, root_y)
        
        for a, b in zip(s1, s2):
            union(a, b)
        return "".join(parent(i) for i in baseStr)
