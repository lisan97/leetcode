class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, k):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type k: int
        :rtype: int
        """
        from collections import defaultdict
        # 状态：起始位置和k
        # 选择：选哪条线路
        # dp[s][k]代表从src出发，k步内到达s的最小路径权重
        # base case:dp[src][...]=0 从 src 到 src，一步都不用走;dp[...][0] = -1:步数用尽，无解
        # 状态转移逻辑:dp[s][k] = min(dp[s1][k-1]+w1,dp[s2][k-1]+w2...)

        # 一次中转会有2条边，所以路径上不能超过 K + 1 条边
        k += 1
        self.src = src
        self.graph = defaultdict(list)
        for edge in flights:
            self.graph[edge[1]].append([edge[0], edge[2]])
        # K 是从 1 开始算的，所以备忘录初始大小要再加一
        self.memo = [[-666] * (k + 1) for _ in range(n)]
        return self.dp(dst, k)

    def dp(self, s, k):
        # 从 src 到 src，一步都不用走
        if s == self.src:
            return 0
        # 如果步数用尽，就无解了
        if k == 0:
            return -1
        if self.memo[s][k] != -666:
            return self.memo[s][k]
        res = float('inf')
        if s in self.graph:
            for edge in self.graph[s]:
                fro = edge[0]
                price = edge[1]
                # src到达上游结点的最小路径权重
                subproblem = self.dp(fro, k - 1)
                # 跳过无解的情况
                if subproblem != -1:
                    res = min(res, subproblem + price)
        # 如果还是初始值，说明此节点不可达
        self.memo[s][k] = res if res != float('inf') else -1
        return self.memo[s][k]