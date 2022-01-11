class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.traverse(root, None, None)

    def traverse(self, root, minval, maxval):
        # 说明全部查完了，都符合要求
        if not root:
            return True
        if minval and root.val <= minval.val:
            return False
        if maxval and root.val >= maxval.val:
            return False
        # 限定左子树的最大值是 root.val，右子树的最小值是 root.val
        # 输出左右子树的检查结果
        return self.traverse(root.left, minval, root) & self.traverse(root.right, root, maxval)