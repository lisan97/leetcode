class Solution(object):
    def movingCount(self, m, n, k):
        """
        :type m: int
        :type n: int
        :type k: int
        :rtype: int
        """
        if m <= 0 or n <= 0 or k < 0:
            return 0
        if k == 0:
            return 1
        self.direction = [-1, 0, 1, 0, -1]
        self.memo = {}
        self.m = m
        self.n = n
        visited = [[False] * n for _ in range(m)]
        self.count = 0
        self.traverse(k, visited, 0, 0)
        return self.count

    def traverse(self, k, visited, i, j):
        if i < 0 or i >= self.m or j < 0 or j >= self.n:
            return
        if visited[i][j]:
            return
        visited[i][j] = True
        self.count += 1
        for a in range(4):
            x = i + self.direction[a]
            y = j + self.direction[a + 1]
            # 要在进入该坐标之前就判断是否符合要求，不符合的话不进入，不然的话比如k=1本来只能访问(1,0),(0,1)，结果能访问到(10,0),(0,10)
            if self.calculate_axis(x, y) <= k:
                self.traverse(k, visited, x, y)

    def calculate_axis(self, i, j):
        if i not in self.memo:
            self.memo[i] = self.calculate(i)
        if j not in self.memo:
            self.memo[j] = self.calculate(j)
        return self.memo[i] + self.memo[j]

    def calculate(self, i):
        res = 0
        while i > 0:
            res += i % 10
            i /= 10
        return res