class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def distanceK(self, root, target, k):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type k: int
        :rtype: List[int]
        """
        from collections import defaultdict,deque
        #根据这棵树构建一张图(字典(list))
        #然后以target为起始进行bfs
        if k == 0:
            return [target.val]
        self.graph = defaultdict(list)
        self.buildGraph(root)
        visited = set()
        if target.val not in self.graph:
            return []
        queue = deque([target.val])
        visited.add(target.val)
        step = 0
        while queue:
            sz = len(queue)
            res = []
            for _ in range(sz):
                node = queue.popleft()
                for neibour in self.graph[node]:
                    if neibour not in visited:
                        queue.append(neibour)
                        res.append(neibour)
                        visited.add(neibour)
            step += 1
            if step == k:
                return res
        return res

    def buildGraph(self,root):
        if root.left:
            self.graph[root.val].append(root.left.val)
            self.graph[root.left.val].append(root.val)
            self.buildGraph(root.left)
        if root.right:
            self.graph[root.val].append(root.right.val)
            self.graph[root.right.val].append(root.val)
            self.buildGraph(root.right)