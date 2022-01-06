class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

#递归
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.res = []
        self.traverse(root)
        return self.res

    def traverse(self, root):
        if not root:
            return
        self.res.append(root.val)
        self.traverse(root.left)
        self.traverse(root.right)

#迭代
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return root
        res = []
        stack = [root]
        while stack:
            node = stack.pop()
            res.append(node.val)
            # 先让右子节点入栈，从而出栈时左子节点先出
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return res

#迭代模板
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        res,stack,node = [],[],root
        while stack or node:
            while node:
                #根节点和左孩子节点入栈
                res.append(node.val)
                stack.append(node)
                node = node.left
            #每弹出一个元素就达到其右子节点
            node = stack.pop()
            node = node.right
        return res

#颜色标记法
class Solution(object):
    def preorderTraversal(self, root):
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
                stack.append((0,node.left))
                stack.append((1,node))
        return res