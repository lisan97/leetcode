class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        '''
        利用二叉搜索树中序遍历递增的特性，中序遍历，计算相邻节点之差
        '''
        self.mindif = float('inf')
        self.pre = -1
        self.traverse(root)
        return self.mindif

    def traverse(self,root):
        if not root:
            return
        self.traverse(root.left)
        if self.pre >= 0:
            self.mindif = min(self.mindif,(root.val-self.pre))
        self.pre = root.val
        self.traverse(root.right)