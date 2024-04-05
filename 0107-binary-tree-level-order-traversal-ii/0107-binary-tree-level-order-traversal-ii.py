# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        sol_arr = [[root.val]]
        queue = deque([root])

        while queue:
            ans = []
            for i in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    ans.append(node.left.val)
                    queue.append(node.left)
                if node.right:
                    ans.append(node.right.val)
                    queue.append(node.right)
            if len(ans) > 0:
                sol_arr.insert(0, ans)
        return sol_arr

        