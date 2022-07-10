class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        #层次遍历记录最大宽度,额外用一个pos来表示
        from collections import deque
        queue = deque([(root,0)])
        res = 0
        while queue:
            sz = len(queue)
            res = max(res,queue[-1][1]-queue[0][1]+1)
            for _ in range(sz):
                node,pos = queue.popleft()
                if node.left:
                    queue.append((node.left,2*pos))
                if node.right:
                    queue.append((node.right,2*pos+1))
        return res
