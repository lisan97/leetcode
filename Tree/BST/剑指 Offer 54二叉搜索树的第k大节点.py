class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def kthLargest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        self.count = 0
        self.val = None
        self.traverse(root, k)
        return self.val

    def traverse(self, root, k):
        if not root or self.val:
            return
        self.traverse(root.right, k)
        self.count += 1
        if self.count == k:
            self.val = root.val
        self.traverse(root.left, k)