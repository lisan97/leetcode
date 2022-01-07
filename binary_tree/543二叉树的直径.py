class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.maxlength = 0
        self.maxDepth(root)
        return self.maxlength

    def maxDepth(self,root):
        if not root:
            return 0
        leftlength = self.maxDepth(root.left)
        rightlength = self.maxDepth(root.right)
        #后序位置顺便计算当前直径(左右子树的深度之和)
        length = leftlength + rightlength
        #更新最大直径
        self.maxlength = max(self.maxlength,length)
        #将当前节点的最大长度返回给父节点
        return max(leftlength,rightlength) + 1