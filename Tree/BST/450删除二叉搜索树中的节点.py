class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        if not root:
            return None
        if root.val == key:
            '''
            这两个条件可以涵盖两种情况：
            1.该节点无子节点
            2.该节点有一个子节点
            '''
            if not root.left:
                return root.right
            if not root.right:
                return root.left
            '''
            3.该节点有两个子节点
            '''
            #找出后继节点(中序遍历的下一个节点，右子树里最小的那个节点)
            minNode = self.getMin(root.right)
            #把 root 改成 后继节点
            root.val = minNode.val
            #删去后继节点
            root.right = self.deleteNode(root.right,minNode.val)
            '''
            #链表操作交换 root 和 minNode 两个节点
            minNode = self.getMin(root.right)
            root.right = self.deleteNode(root.right,minNode.val)
            minNode.left = root.left
            minNode.right = root.right
            root = minNode
            '''
        elif root.val > key:
            root.left = self.deleteNode(root.left,key)
        else:
            root.right = self.deleteNode(root.right,key)
        return root

    def getMin(self,node):
        #最左边的就是最小的
        while node.left:
            node = node.left
        return node
