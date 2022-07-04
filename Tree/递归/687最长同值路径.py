# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = 0
        self.longest(root)
        return self.res

    #返回以当前节点的最长路径长度
    def longest(self,root):
        if not root:
            return 0
        left = self.longest(root.left)
        right = self.longest(root.right)
        if not root.left or root.val != root.left.val:
            left = 0
        else:
            left += 1
        if not root.right or root.val != root.right.val:
            right = 0
        else:
            right += 1
        self.res = max(self.res,left + right)
        return max(left,right)