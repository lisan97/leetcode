# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        self.res = []
        track = [str(root.val)]
        self.traverse(root, track)
        return self.res

    def traverse(self, root, track):
        if not root.left and not root.right:
            self.res.append('->'.join(track))
            return
        if root.left:
            track.append(str(root.left.val))
            self.traverse(root.left, track)
            track.pop()
        if root.right:
            track.append(str(root.right.val))
            self.traverse(root.right, track)
            track.pop()