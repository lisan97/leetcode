from UF import UF
class Solution(object):
    def minimumCost(self, n, connections):
        """
        :type n: int
        :type edges: List[List[str]]
        :rtype: int
        """
        '''
        将所有边按照权重从小到大排序，从权重最小的边开始遍历，
        如果这条边和mst中的其它边不会形成环，则这条边是最小生成树的一部分，将它加入mst集合；
        否则，这条边不是最小生成树的一部分，不要把它加入mst集合。
        '''
        uf = UF(n)
        total = 0
        #对所有边按照权重从小到大排序
        connections = sorted(connections,key=lambda x: x[2])
        for edge in connections:
            p,q,cost = edge[0]-1, edge[1]-1, edge[2]
            # 若这条边会产生环，则不能加入 mst
            if not uf.connected(p,q):
                #若这条边不会产生环，则属于最小生成树
                uf.union(p,q)
                total += cost
        #保证所有节点都被连通
        return total if uf.Count() == 1 else -1

if __name__ == '__main__':
    n = 3
    connections = [[1,2,5],[1,3,6],[2,3,1]]
    S = Solution()
    print(S.minimumCost(n,connections))