class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        if not matrix:
            return 0
        self.directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        self.m = len(matrix)
        self.n = len(matrix[0])
        self.memo = {}
        maxlen = -1
        for i in range(self.m):
            for j in range(self.n):
                maxlen = max(maxlen, self.dfs(i, j, matrix))
        return maxlen

    def dfs(self, i, j, matrix):
        if (i, j) in self.memo:
            return self.memo[(i, j)]
        res = 1
        for dx, dy in self.directions:
            x, y = i + dx, j + dy
            if x >= 0 and x < self.m and y >= 0 and y < self.n and matrix[x][y] > matrix[i][j]:
                res = max(res, self.dfs(x, y, matrix) + 1)
        self.memo[(i, j)] = res
        return res