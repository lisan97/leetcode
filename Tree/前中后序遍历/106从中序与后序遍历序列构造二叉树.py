class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if not inorder:
            return None
        #根节点对应的值为 postorder 的最后一个元素
        root = TreeNode(postorder[-1])
        mid = inorder.index(root.val)
        #确定后序遍历左右子树的思路：
        #1.根据左-右-根，左子树也是[:mid]，右子树是左子树(mid)和根节点(-1)之间
        #2.根节点对应的值为 postorder 的最后一个元素
        root.left = self.buildTree(inorder[:mid],postorder[:mid])
        root.right = self.buildTree(inorder[mid+1:],postorder[mid:-1])
        return root


class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        self.dic = {}
        for k, v in enumerate(inorder):
            self.dic[v] = k
        n = len(inorder)
        return self.traverse(inorder, 0, n - 1, postorder, 0, n - 1)

    def traverse(self, inorder, inleft, inright, postorder, postleft, postright):
        if postleft > postright or inleft > inright:
            return None
        postroot = postorder[postright]
        inroot = self.dic[postroot]
        root = TreeNode(postroot)
        rightsize = inright - (inroot + 1)  # 右子树的大小
        root.left = self.traverse(inorder, inleft, inroot - 1, postorder, postleft, postright - 2 - rightsize)
        root.right = self.traverse(inorder, inroot + 1, inright, postorder, postright - 1 - rightsize, postright - 1)
        return root