class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if "0000" in deadends:
            return -1
        queue = deque()
        queue.append(["0000", 0])
        visited = set(deadends)

        def nexts(lock):
            res = []
            for i in range(4):
                ch = str((int(lock[i])+1) % 10)
                new_l = lock[:i] + ch + lock[i+1:]
                res.append(new_l)

                ch = str(((int(lock[i])-1)+10) % 10)
                new_l = lock[:i] + ch + lock[i+1:]
                res.append(new_l)
            return res
        while queue:
            w, t = queue.popleft()

            if w == target:
                return t
            for next_w in nexts(w):
                if next_w not in visited:
                    queue.append([next_w, t + 1])
                    visited.add(next_w)
        return -1
        