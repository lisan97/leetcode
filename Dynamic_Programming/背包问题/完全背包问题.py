#dp[i][j] = max(dp[i-1][j], dp[i][j-w] + v)
class Solution(object):
    def backpack(self, N,W,wt,val):
        dp = [[0]*(N+1) for _ in range(W+1)]
        for i in range(1,N+1):
            for j in range(1,W+1):
                if j < wt[i-1]:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = max(dp[i-1][j],dp[i][j-wt[i-1]]+val[i-1])
        return dp[-1][-1]

#状态压缩
class Solution(object):
    def backpack(self, N,W,wt,val):
        dp = [0] * (W+1)
        for i in range(1,N+1):
            w = wt[i-1]
            v = val[i-1]
            #我们在遍历每一行的时候必须正向遍历
            for j in range(w,W+1):
                dp[j] = max(dp[j-w]+v,dp[j])
        return dp[-1]