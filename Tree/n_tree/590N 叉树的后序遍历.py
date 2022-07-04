class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children




class Solution(object):
    def postorder(self, root):
        """
        :type
        root: Node
        :rtype: List[int]
        """
        self.res = []
        self.traverse(root)
        return self.res

    def traverse(self,root):
        if not root:
            return
        for node in root.children:
            self.traverse(node)
        self.res.append(root.val)