class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def constructFromPrePost(self, preorder, postorder):
        """
        :type preorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if not preorder:
            return None
        #防止preorder只有一个值，取leftid 超出index的情况
        if len(preorder) == 1:
            return TreeNode(preorder[0])
        root = TreeNode(preorder[0])
        #先序遍历的第二个节点是左子树的根节点，在后序遍历中位于左子树的最后一个，可以用来分割左右子树
        leftid = postorder.index(preorder[1])
        root.left = self.constructFromPrePost(preorder[1:leftid+2],postorder[:leftid+1])
        root.right = self.constructFromPrePost(preorder[leftid+2:],postorder[leftid+1:-1])
        return root