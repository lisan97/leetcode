class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

#递归
class Solution(object):
    def postorderTraversal(self, root):
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
        self.traverse(root.left)
        self.traverse(root.right)
        self.res.append(root.val)

#迭代
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        res, stack, node = [],[],root
        #按 根-右-左的顺序加入，然后反转输出结果
        while stack or node:
            while node:
                res.append(node.val)
                stack.append(node)
                node = node.right
            node = stack.pop()
            node = node.left
        return res[::-1]

#标记法，模拟真实入栈顺序
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        stack,res = [(0,root)],[]
        while stack:
            label, node = stack.pop()
            if not node:
                continue
            #已经遍历过了，加入到结果
            if label == 1:
                res.append(node.val)
            else:
                stack.append((1,node))
                stack.append((0,node.right))
                stack.append((0,node.left))
        return res