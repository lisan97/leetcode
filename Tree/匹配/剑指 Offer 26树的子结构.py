class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isSubStructure(self, A, B):
        """
        :type A: TreeNode
        :type B: TreeNode
        :rtype: bool
        """
        '''
        和572的区别是B 属于 A 的一部分也可以，没必要一直匹配到叶子节点，因此修改isSametree函数的条件即可。
        '''
        #空树不是任意一个树的子结构
        if not A or not B:
            return False
        return self.isSametree(A,B) or self.isSubStructure(A.left,B) or self.isSubStructure(A.right,B)

    def isSametree(self,A,B):
        #说明B已经完成匹配
        if not B:
            return True
        if not A:
            return False
        if A.val != B.val:
            return False
        return self.isSametree(A.left,B.left) and self.isSametree(A.right,B.right)