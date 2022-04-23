class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return root
        #root 节点需要交换它的左右子节点
        #放在前序或后序位置都行，无非是先交换最上面的子节点还是先交换最底部的子节点
        root.left,root.right = root.right, root.left
        #让左右子节点继续翻转它们的子节点
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root