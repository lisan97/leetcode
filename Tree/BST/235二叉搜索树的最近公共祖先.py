class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        #如果当前节点的值不满足上述两条要求，那么说明当前节点就是「分岔点」
        min_val = min(p.val,q.val)
        max_val = max(p.val,q.val)
        return self.helper(root,min_val,max_val)

    def helper(self,root,min_val,max_val):
        if not root:
            return None
        if root.val < min_val:
            return self.helper(root.right,min_val,max_val)
        if root.val > max_val:
            return self.helper(root.left,min_val,max_val)
        return root

#迭代写法
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        min_val = min(p.val,q.val)
        max_val = max(p.val,q.val)
        while root:
            if root.val < min_val:
                root = root.right
            elif root.val > max_val:
                root = root.left
            else:
                return root
        return None