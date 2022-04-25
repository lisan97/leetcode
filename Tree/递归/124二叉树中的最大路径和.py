class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root.left and not root.right:
            return root.val
        self.maxSum = float('-inf')
        self.traverse(root)
        return self.maxSum

    def traverse(self, root):
        # base case
        if not root:
            return 0
        # 递归计算左右子节点的最大贡献值
        # 负数处理：只有在最大贡献值大于 0 时，才会选取对应子节点
        leftSum = max(0, self.traverse(root.left))
        rightSum = max(0, self.traverse(root.right))
        # 当前节点的最大路径和取决于该节点的值与该节点的左右子节点的最大贡献值
        tmp = root.val + leftSum + rightSum
        # 更新答案
        self.maxSum = max(tmp, self.maxSum)
        # 因为一个节点只能选择2个方向（左右or左上or右上）
        # 因此返回给父节点时左右只能选一条路径，返回节点的最大贡献值
        return max(leftSum, rightSum) + root.val