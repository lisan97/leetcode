class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = []
        track = []
        self.traverse(root,track)
        return sum(self.res)

    def traverse(self,root,track):
        if not root:
            return
        track.append(str(root.val))
        if not root.left and not root.right:
            self.res.append(int(''.join(track)))
            track.pop()
            return
        self.traverse(root.left,track)
        self.traverse(root.right,track)
        track.pop()