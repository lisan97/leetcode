class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        G = [0] * (n+1)
        #根节点和空树都算作一种情况
        G[0]  = G[1] = 1
        #计算长度为n的序列能构成的不同二叉搜索树的个数
        for i in range(2,n+1):
            #以不同节点为根节点的情况求和
            for j in range(1,i+1):
                G[i] += G[j-1]*G[i-j]
        return G[n]