from UF import UF

class Solution(object):
    def minCostConnectPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        #思路就是先生成所有的边以及权重，然后对这些边执行 Kruskal 算法即可
        n = len(points)
        if n == 1:
            return 0
        edges = []
        for i in range(n):
            p = points[i]
            xi = p[0]
            yi = p[1]
            for j in range(i+1,n):
                q = points[j]
                xj = q[0]
                yj = q[1]
                edges.append([i,j,abs(xi-xj)+abs(yi-yj)])
        edges = sorted(edges,key = lambda x:x[2])
        uf = UF(n)
        total = 0
        for edge in edges:
            p,q,cost = edge[0],edge[1],edge[2]
            if not uf.connected(p,q):
                uf.union(p,q)
                total += cost
        return total