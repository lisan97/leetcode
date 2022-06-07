class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not preorder:
            return None
        #前序遍历的第一个结点就是根节点
        root = TreeNode(preorder[0])
        #找到中序遍历对应的根节点的索引(左边就是左子树，右边就是右子树)
        mid = inorder.index(root.val)
        #递归构造左右子树
        #确定先序遍历左右子树位置的思路
        #1.因为前序是根左右，中序是左根右，所以前序遍历和中序遍历mid+1的左边肯定都是根和左子树，那么mid+1右侧的便是右子树了
        #2.先序遍历可以通过左子树的节点数(leftsize)推导出来
        root.left = self.buildTree(preorder[1:mid+1],inorder[:mid])
        root.right = self.buildTree(preorder[mid+1:],inorder[mid+1:])
        return root

#O(n)用哈希表把中序遍历每个值的索引记下来
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not preorder:
            return
        self.dic = {v:k for k,v in enumerate(inorder)}
        n = len(preorder)
        return self.traverse(preorder,0,n-1,inorder,0,n-1)

    def traverse(self,preorder,preLeft,preRight,inorder,inLeft,inRight):
        if preLeft > preRight:
            return None
        preRoot = preLeft
        inRoot = self.dic[preorder[preRoot]]
        root = TreeNode(preorder[preRoot])
        leftSize = inRoot-inLeft
        root.left = self.traverse(preorder,preLeft+1,preLeft+leftSize,inorder,inLeft,inRoot-1)
        root.right = self.traverse(preorder,preLeft+1+leftSize,preRight,inorder,inRoot+1,inRight)
        return root