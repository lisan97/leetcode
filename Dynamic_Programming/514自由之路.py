class Solution(object):
    def findRotateSteps(self, ring, key):
        """
        :type ring: str
        :type key: str
        :rtype: int
        """
        from collections import defaultdict
        self.m = len(ring)
        self.n = len(key)
        self.key = key
        self.memo = [[0]*self.n for _ in range(self.m)]
        #记录圆环上字符到索引的映射
        self.char2index = defaultdict(list)
        for i in range(self.m):
            self.char2index[ring[i]].append(i)
        #圆盘指针最初指向 12 点钟方向，从第一个字符开始输入 key
        return self.dp(0,0)

    #计算圆盘指针在 ring[i]，输入 key[j..] 的最少操作数
    def dp(self,i,j):
        #base case 完成输入
        if j == self.n:
            return 0
        if self.memo[i][j] != 0:
            return self.memo[i][j]
        res = float('inf')
        #ring 上可能有多个字符 key[j]
        for k in self.char2index[self.key[j]]:
            #拨动指针的次数
            delta = abs(k-i)
            #选择顺时针还是逆时针
            delta = min(delta, self.m-delta)
            #将指针拨到 ring[k]，继续输入 key[j+1..]
            subproblem = self.dp(k,j+1)
            #选择「整体」操作次数最少的,加一是因为按动按钮也是一次操作
            res = min(res,1+delta+subproblem)
        self.memo[i][j] = res
        return self.memo[i][j]