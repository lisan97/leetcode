class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return None
        self.connectTwoNode(root.left,root.right)
        return root
    #只依赖一个节点的话，肯定是没办法连接「跨父节点」的两个相邻节点
    #因此想到需要增加辅助函数，给他安排两个节点
    def connectTwoNode(self,node1,node2):
        if not node1 or not node2:
            return
        #将传入的两个节点连接
        node1.next = node2
        #连接相同父节点的两个子节点
        self.connectTwoNode(node1.left,node1.right)
        self.connectTwoNode(node2.left,node2.right)
        #连接跨越父节点的两个子节点
        self.connectTwoNode(node1.right,node2.left)