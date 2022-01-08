class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

#先序遍历把所有node放在一个列表，然后开始一个一个连
#空间复杂度O(n)
class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        self.nodeList = []
        self.traverse(root)
        for i in range(1,len(self.nodeList)):
            pre,cur = self.nodeList[i-1],self.nodeList[i]
            pre.left = None
            pre.right = cur
        return root

    def traverse(self, root):
        if not root:
            return
        self.nodeList.append(root)
        self.traverse(root.left)
        self.traverse(root.right)

#递归解法
class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        if not root:
            return []
        self.flatten(root.left)
        self.flatten(root.right)
        #后序遍历：因为我们要先拉平左右子树才能进行后续操作
        #1、左右子树已经被拉平成一条链表
        left = root.left
        right = root.right
        #2、将左子树作为右子树
        root.left = None
        root.right = left
        #3、将原先的右子树接到当前右子树的末端
        p = root
        while p.right:
            p = p.right
        p.right = right

        return root