class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        #记录累加和
        self.sum = 0
        self.traverse(root)
        return root

    def traverse(self,root):
        if not root:
            return None
        self.traverse(root.right)
        #维护累加和
        self.sum += root.val
        #将 BST 转化成累加树
        root.val = self.sum
        self.traverse(root.left)