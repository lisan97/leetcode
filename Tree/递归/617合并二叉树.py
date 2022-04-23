class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def mergeTrees(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: TreeNode
        """
        '''
        将root2覆盖到root1上
        '''
        #都没有return None
        if not root1 and not root2:
            return None
        #没有root1 return root2
        if not root1:
            return root2
        #没有root2 return root1
        if not root2:
            return root1
        #都有的情况，两个值相加
        root1.val = root1.val + root2.val
        #递归求左右子树
        root1.left = self.mergeTrees(root1.left,root2.left)
        root1.right = self.mergeTrees(root1.right,root2.right)
        return root1