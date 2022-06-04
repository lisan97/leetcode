class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        #层次遍历，每层只保留最后一个
        if not root:
            return
        from collections import deque
        queue = deque([root])
        res = []
        while queue:
            sz = len(queue)
            for _ in range(sz):
                node = queue.popleft()
                tmp = node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(tmp)
        return res