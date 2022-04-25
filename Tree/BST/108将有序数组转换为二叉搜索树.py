class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        return self.helper(nums, 0, len(nums) - 1)

    # 通过找到数组的中点确定父节点，然后递归求解左右子树
    def helper(self, nums, l, r):
        if l > r:
            return None
        mid = (l + r) // 2
        root = TreeNode(val=nums[mid])
        root.left = self.helper(nums, l, mid - 1)
        root.right = self.helper(nums, mid + 1, r)
        return root