class Solution(object):
    def backpack(self, N,W,wt,val):
        #状态有两个，就是「背包的容量」和「可选择的物品」
        dp = [[0]*(W+1) for _ in range(N+1)]
        for n in range(1,N+1):
            for w in range(1,W+1):
                if w - wt[n-1] < 0:
                    #这种情况下只能选择不装入背包
                    dp[n][w] = dp[n-1][w]
                else:
                    #选择：装入或者不装入背包，择优
                    dp[n][w] = max(dp[n-1][w-wt[n-1]]+val[n-1],dp[n-1][w])
        return dp[-1][-1]

if __name__ == '__main__':
    N = 3
    W = 4
    wt = [2, 1, 3]
    val = [4, 2, 3]
    print(Solution().backpack(N,W,wt,val))