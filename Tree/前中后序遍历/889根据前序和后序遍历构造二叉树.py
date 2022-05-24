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
        #我们假设前序遍历的第二个元素是左子树的根节点，但实际上左子树可能是空指针，这个元素可能是右子树的根节点。
        #由于这里无法确切进行判断，所以导致了最终答案的不唯一。
        root = TreeNode(preorder[0])
        #先序遍历的第二个节点是左子树的根节点，在后序遍历中位于左子树的最后一个，可以用来分割左右子树
        leftid = postorder.index(preorder[1])
        root.left = self.constructFromPrePost(preorder[1:leftid+2],postorder[:leftid+1])
        root.right = self.constructFromPrePost(preorder[leftid+2:],postorder[leftid+1:-1])
        return root

class Solution(object):
    def constructFromPrePost(self, preorder, postorder):
        """
        :type preorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if not preorder:
            return []
        self.dic = {}
        for k,v in enumerate(postorder):
            self.dic[v] = k
        n = len(postorder)
        return self.traverse(preorder,0,n-1,postorder,0,n-1)

    def traverse(self,preorder,preleft,preright,postorder,postleft,postright):
        if preleft > preright or postleft > postright:
            return None
        if preleft == preright or postleft == postright:
            return TreeNode(preorder[preleft])
        root = TreeNode(preorder[preleft])
        leftid = self.dic[preorder[preleft+1]]
        leftsize = leftid - postleft #左子树的大小
        root.left = self.traverse(preorder,preleft+1,preleft+leftsize+1,postorder,postleft,leftid)
        root.right = self.traverse(preorder,preleft+leftsize+2,preright,postorder,leftid+1,postright-1)
        return root