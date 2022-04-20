class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def delNodes(self, root, to_delete):
        """
        :type root: TreeNode
        :type to_delete: List[int]
        :rtype: List[TreeNode]
        """
        self.to_delete = set(to_delete)
        self.forest = []
        root = self.helper(root)
        if root:
            self.forest.append(root)
        return self.forest

    def helper(self,root):
        if not root:
            return root
        root.left = self.helper(root.left)
        root.right = self.helper(root.right)
        #如果当前val在delete set里面，先将左右子树放入forest，然后将该点设为None
        if root.val in self.to_delete:
            if root.left:
                self.forest.append(root.left)
            if root.right:
                self.forest.append(root.right)
            root = None
        return root