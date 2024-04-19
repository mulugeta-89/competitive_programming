# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        sol = []
        def bfs(root):
            queue = deque()
            queue.append(root)
            sol.append(root.val/1)

            while queue:
                small = []
                for i in range(len(queue)):
                    node = queue.popleft()

                    if node.left:
                        small.append(node.left.val)
                        queue.append(node.left)
                    if node.right:
                        small.append(node.right.val)
                        queue.append(node.right)
                if len(small) > 0:
                    sol.append(sum(small)/len(small))
        bfs(root)
        return sol



        