class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
#遍历计数，O(n)
class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)

#follow up
#普通二叉树和完全二叉树的结合版
#O(logN*logN)
class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        '''
        由于完全二叉树的性质，每个节点里两棵子树一定有一棵是满的，所以一定会触发 hl == hr，只消耗 O(logN) 的复杂度而不会继续递归
        因此算法的递归深度就是树的高度 O(logN)，每次递归所花费的时间就是 while 循环，也需要 O(logN)，所以总体的时间复杂度是 O(logN*logN)
        '''
        if not root:
            return 0
        left,right = root,root
        hl , hr = 0,0
        while left:
            left = left.left
            hl += 1
        while right:
            right = right.right
            hr += 1
        #如果左右子树的高度相同，则是一棵满二叉树
        if hl == hr:
            return 2 ** hl - 1
        #如果左右高度不同，则按照普通二叉树的逻辑计算
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)