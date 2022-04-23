class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: int
        """
        # 如果不选取该节点加入路径，则对其左右节点进行重新进行考虑。
        if not root:
            return 0
        return self.pathcount(root, targetSum) + self.pathSum(root.left, targetSum) + self.pathSum(root.right,
                                                                                                   targetSum)

    # 统计以某个root为起始节点的路径数
    def pathcount(self, root, targetSum):
        if not root:
            return 0
        count = 1 if targetSum == root.val else 0
        count += self.pathcount(root.left, targetSum - root.val)
        count += self.pathcount(root.right, targetSum - root.val)
        return count