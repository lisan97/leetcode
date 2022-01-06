class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

#遍历一遍二叉树
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # 记录最大深度
        self.res = 0
        # 记录遍历到的节点的深度
        self.depth = 0
        self.reverse(root)
        return self.res

    def reverse(self, root):
        if not root:
            # 到达叶子节点，更新最大深度
            self.res = max(self.res, self.depth)
            return
        # 前序位置，从父节点进入子节点，深度+1
        self.depth += 1
        self.reverse(root.left)
        self.reverse(root.right)
        # 后序位置，离开子节点返回其父节点，深度-1
        self.depth -= 1

#分解问题
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        #利用定义，计算左右子树的最大深度
        leftDepth = self.maxDepth(root.left)
        rightDepth = self.maxDepth(root.right)
        '''
        为什么主要的代码逻辑集中在后序位置？
        因为需要首先利用递归函数的定义算出左右子树的最大深度，然后推出原树的最大深度，主要逻辑自然放在后序位置。
        整棵树的最大深度等于左右子树的最大深度取最大值，然后再加上根节点自己
        '''
        depth = max(leftDepth, rightDepth) + 1
        return depth