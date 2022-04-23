# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def trimBST(self, root, low, high):
        """
        :type root: TreeNode
        :type low: int
        :type high: int
        :rtype: TreeNode
        """
        '''
        使用前序遍历，在到达父节点时就进行判断，从而决定对当前及子树的裁剪操作
        '''
        if not root:
            return root
        #如果当前val比low小，那么修剪后的子树必定在它右边
        if root.val < low:
            return self.trimBST(root.right,low,high)
        #如果当前val比high大，那么修剪后的子树必定在它左边
        if root.val > high:
            return self.trimBST(root.left,low,high)
        root.left = self.trimBST(root.left,low,high)
        root.right = self.trimBST(root.right,low,high)
        return root