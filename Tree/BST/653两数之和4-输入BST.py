class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        self.array = []
        self.traverse(root)
        i = 0
        j = len(self.array) - 1
        while i < j:
            total = self.array[i] + self.array[j]
            if total > k:
                j -= 1
            elif total < k:
                i += 1
            else:
                return True
        return False

    def traverse(self,root):
        if not root:
            return
        self.traverse(root.left)
        self.array.append(root.val)
        self.traverse(root.right)