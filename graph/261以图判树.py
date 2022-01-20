from UF import UF

class Solution(object):
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[str]]
        :rtype: bool
        """
        '''
        对于添加的这条边，如果该边的两个节点本来就在同一连通分量里，那么添加这条边会产生环；
        反之，如果该边的两个节点不在同一连通分量里，则添加这条边不会产生环。
        '''
        uf = UF(n)
        for edge in edges:
            p,q = edge[0],edge[1]
            #若两个节点已经在同一连通分量中，会产生环
            if uf.connected(p,q):
                return False
            uf.union(p,q)
        #要保证最后只形成了一棵树，即只有一个连通分量
        return uf.Count() == 1

if __name__ == '__main__':
    n = 5
    edges = [[0, 1], [0, 2], [0, 3], [1, 4]]
    #edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]
    S = Solution()
    print(S.validTree(n,edges))