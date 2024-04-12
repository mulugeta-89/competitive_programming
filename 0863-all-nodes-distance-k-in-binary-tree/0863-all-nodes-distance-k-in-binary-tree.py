# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
    
        graph = defaultdict(list)
        self.buildGraph(root, None, graph)
        queue = deque()
        queue.append([target, 0])
        visited = set()
        visited.add(target)
        answer = []
        while queue:
            node, distance = queue.popleft()
            if k == distance:
                answer.append(node.val)
            
            if distance < k:
                for neighbour in graph[node]:
                    if neighbour not in visited:
                        queue.append([neighbour, distance+1])
                        visited.add(neighbour)

        return answer

    def buildGraph(self, node, parent, graph):
        if node is None:
            return
        if parent is not None:
            graph[node].append(parent)
        if node.left:
            graph[node].append(node.left)
            self.buildGraph(node.left, node, graph)
        if node.right:
            graph[node].append(node.right)
            self.buildGraph(node.right, node, graph)
                

        