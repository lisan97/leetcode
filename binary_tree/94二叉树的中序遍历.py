class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

#递归
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.res = []
        self.traverse(root)
        return self.res

    def traverse(self,root):
        if not root:
            return
        self.traverse(root.left)
        self.res.append(root.val)
        self.traverse(root.right)

#迭代
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        res,stack,node = [], [], root
        while node or stack:
            while node:
                #入栈，到达最左端的叶子节点
                stack.append(node)
                node = node.left
            node = stack.pop()
            #出栈时再加入结果
            res.append(node.val)
            node = node.right
        return res

#颜色标记法
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        res,stack = [],[(0,root)]
        while stack:
            label, node = stack.pop()
            if not node:
                continue
            if label == 1:
                res.append(node.val)
            else:
                stack.append((0,node.right))
                stack.append((1,node))
                stack.append((0,node.left))
        return res