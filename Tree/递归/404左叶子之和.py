class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.helper(root,False)
    #在辅函数里多传一个参数，表示当前节点是不是父节点的左节点。
    def helper(self,root,isleft):
        if not root:
            return 0
        if not root.left and not root.right and isleft:
            return root.val
        return self.helper(root.left,True) + self.helper(root.right,False)