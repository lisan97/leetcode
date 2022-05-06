class Solution(object):
    def verifyPostorder(self, postorder):
        """
        :type postorder: List[int]
        :rtype: bool
        """
        '''
        最后一个节点是根节点，前面应该分为两段，右子树全比根节点大，左子树全比根节点小
        从前往后遍历，找到左右子树的分割点，然后去判断右子树里有没有比根节点小的；
        然后递归地去判断左右子树是否正确
        '''
        if not postorder:
            return True
        length = len(postorder)
        root = postorder[length-1]
        i = 0
        #找到第一个比root大的结点作为右子树的起点
        while i < length - 1:
            if postorder[i] > root:
                break
            i += 1
        j = i
        #若右子树中有一个结点比root小，return False
        while j < length - 1:
            if postorder[j] < root:
                return False
            j += 1
        left = True
        #如果有左子树，递归去检测左子树
        if i > 0:
            left = self.verifyPostorder(postorder[:i])
        right = True
        #如果有右子树，递归检测右子树
        if i < length - 1:
            right = self.verifyPostorder(postorder[i:length-1])
        return left and right