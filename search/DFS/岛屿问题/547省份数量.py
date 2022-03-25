class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        '''
        主函数用于遍历所有的搜索位置，判断是否可以开始搜索，如果可以即在辅函数进行搜索。
        辅函数则负责深度优先搜索的递归调用。
        本题图的表示：每一行（列）表示一个节点，它的每列（行）表示是否存在一个相邻节点
        '''
        self.m = len(isConnected)
        res = 0
        #记录该节点有没有被访问过
        visited = [False] * self.m
        for i in range(self.m):
            if not visited[i]:
                self.dfs(isConnected,i,visited)
                #dfs结束代表访问遍了这个节点能到达的节点
                res += 1
        return res

    def dfs(self,isConnected,i,visited):
        visited[i] = True
        #访问该节点的邻居
        for j in range(self.m):
            if not visited[j] and isConnected[i][j] == 1:
                self.dfs(isConnected,j,visited)