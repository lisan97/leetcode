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

#状态压缩
# n只依赖n-1的信息，之前算过的其他物品都不需要再使用。
# 因此我们可以去掉 dp 矩阵的第一个维度，在考虑物品 i 时变成 dp[j] = max(dp[j], dp[j-w] + v)
class Solution(object):
    def backpack(self, N,W,wt,val):
        dp = [0] * (W+1)
        for i in range(N):
            w = wt[i]
            v = val[i]
            #在遍历每一行的时候必须逆向遍历，这样才能够调用上一行物品 i-1 时 dp[j-w] 的值
            for j in range(W,w-1,-1):
                dp[j] = max(dp[j-w]+v,dp[j])
        return dp[-1]

if __name__ == '__main__':
    N = 3
    W = 4
    wt = [2, 1, 3]
    val = [4, 2, 3]
    print(Solution().backpack(N,W,wt,val))