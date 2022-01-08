class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None
        maxValue = float('-inf')
        idx = 0
        #找到数组中的最大值和其索引
        for i in range(len(nums)):
            if nums[i] > maxValue:
                idx = i
                maxValue = nums[i]
        root = TreeNode(val = maxValue)
        #递归调用构造左右子树
        root.left = self.constructMaximumBinaryTree(nums[:idx])
        root.right = self.constructMaximumBinaryTree(nums[idx+1:])
        return root