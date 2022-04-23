class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def isSubtree(self, root, subRoot):
        """
        :type root: TreeNode
        :type subRoot: TreeNode
        :rtype: bool
        """
        '''
        断 t 是否为 s 的子树的三个条件是或的关系，即：
        1.当前两棵树相等；
        2.或者，t 是 s 的左子树；
        3.或者，t 是 s 的右子树。
        '''
        if not root and not subRoot:
            return True
        if not root or not subRoot:
            return False
        return self.isSametree(root,subRoot) or self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)

    def isSametree(self,left,right):
        if not left and not right:
            return True
        if not left or not right:
            return False
        if left.val != right.val:
            return False
        return self.isSametree(left.left,right.left) and self.isSametree(left.right,right.right)