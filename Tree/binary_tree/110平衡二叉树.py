class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.help(root) != -1

    def help(self,root):
        if not root:
            return 0
        #求每个子树的深度
        left = self.help(root.left)
        right = self.help(root.right)
        #若子树已经不符合平衡二叉树了，直接返回-1
        if left == -1 or right == -1 or abs(left-right)>1:
            return -1
        return 1 + max(left,right)