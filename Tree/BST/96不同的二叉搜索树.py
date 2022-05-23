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

class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        #备忘录消除重叠子问题
        self.memo = {}
        return self.count(1,n)

    #计算闭区间 [lo, hi] 组成的 BST 个数
    def count(self,l,r):
        #base case
        if l > r:
            return 1
        if (l,r) in self.memo:
            return self.memo[(l,r)]
        res = 0
        for mid in range(l,r+1):
            #mid的值作为根节点 root
            left = self.count(l,mid-1)
            right = self.count(mid+1,r)
            #左右子树的组合数乘积是以mid为根节点的BST的总数
            res += left * right
        self.memo[(l,r)] = res
        return res