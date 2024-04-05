# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        sol_arr = [[root.val]]
        queue = deque([root])
        while queue:
            n  = len(queue)
            arr = []
            for i in range(n):
                node = queue.popleft()
                if node.left:
                    arr.append(node.left.val)
                    queue.append(node.left)
                if node.right:
                    arr.append(node.right.val)
                    queue.append(node.right)
            if len(arr) > 0:
                sol_arr.append(arr)
        return sol_arr
        