class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        from collections import deque
        res = []
        q = deque([root])
        while q:
            size = len(q)
            stack = []
            for _ in range(size):
                node = q.popleft()
                stack.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(sum(stack)/float(size))
        return res