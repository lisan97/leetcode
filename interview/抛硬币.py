'''
给定一枚不均匀硬币，抛出正面的概率为P，求抛2K+1至多有K次出现正面的概率
'''
def throwcoin(p,k):
    #dp[i][j]代表出现i次正面k次反面的概率
    #base case:dp[i][j]=1
    #状态转移：dp[i][j] = p * dp[i-1][j] + (1-p) * dp[i][j-1]
    dp = [[0] * (2*k+2) for _ in range(2*k+2)]
    dp[0][0] = 1
    dp[1][0] = p
    dp[0][1] = 1-p
    for i in range(1,2*k+2):
        for j in range(1,2*k+2):
            dp[i][j] = p * dp[i-1][j] + (1-p) * dp[i][j-1]
    return dp