class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        #用一个dummy节点记录root的前一个节点
        dummy = TreeNode(val=0)
        self.pre = dummy
        self.helper(root)
        return dummy.right


    def helper(self,root):
        if not root:
            return root
        self.helper(root.left)
        root.left=None #root的left就是pre
        self.pre.right = root
        self.pre = self.pre.right
        self.helper(root.right)