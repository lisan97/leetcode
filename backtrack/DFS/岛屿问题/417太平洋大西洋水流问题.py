class Solution(object):
    def pacificAtlantic(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: List[List[int]]
        """
        '''
        可以反过来想，从两个大洋开始向上流，这样我们只需要对矩形四条边进行搜索。
        搜索完成后，只需遍历一遍矩阵，满足条件的位置即为两个大洋向上流都能到达的位置。
        '''
        self.m = len(heights)
        self.n = len(heights[0])
        res = []
        if self.m == 1 or self.n == 1:
            for i in range(self.m):
                for j in range(self.n):
                    res.append([i,j])
            return res
        #对于四个方向的遍历，可以创造一个数组 [-1, 0, 1, 0, -1]，每相邻两位即为上下左右四个方向之一
        self.direction = [-1,0,1,0,-1]
        reach_p = [[False] * self.n for _ in range(self.m)]
        reach_a = [[False] * self.n for _ in range(self.m)]
        for j in range(self.n):
            self.dfs(heights,0,j,reach_p)
            self.dfs(heights,self.m-1,j,reach_a)
        for i in range(self.m):
            self.dfs(heights,i,0,reach_p)
            self.dfs(heights,i,self.n-1,reach_a)
        for i in range(self.m):
            for j in range(self.n):
                #二者都能达到的节点
                if reach_a[i][j] and reach_p[i][j]:
                    res.append([i,j])
        return res

    def dfs(self,heights,i,j,reach):
        if reach[i][j]:
            return
        reach[i][j] = True
        for a in range(4):
            x = i + self.direction[a]
            y = j + self.direction[a+1]
            if x >= 0 and x < self.m and y >= 0 and y < self.n and heights[i][j] <= heights[x][y]:
                self.dfs(heights,x,y,reach)