class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # 递归地拿左子树的左节点和右子树的右节点；左子树的右节点和右子树的左节点做比较
        if not root:
            return True
        return self.help(root.left, root.right)

    def help(self, left, right):
        if not left and not right:
            return True
        if not left or not right:
            return False
        if left.val != right.val:
            return False
        return self.help(left.left, right.right) and self.help(left.right, right.left)