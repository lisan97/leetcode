#思路1 复杂度较高会超时O(N^3)
#状态有3个：剩余按键次数n；当前屏幕全部的A的数量a_num；当前缓冲区A的数量copy
#选择：四个按键
#dp
#base case:当n==0时，此时的a_num就是我们想要的答案
#状态转移：dp[n][a_num][copy] = dp[n-1][a_num+1][copy] A
#                              dp[n-1][a_num+copy][copy] #ctrl+v
#                              dp[n-1][a_num][a_num] #ctrl+A ctrl+c
#看这个穷举逻辑，是有可能出现这样的操作序列 C-A C-C，C-A C-C... 或者 C-V,C-V,...。然这种操作序列的结果不是最优的，但是我们并没有想办法规避这些情况的发生，从而增加了很多没必要的子问题计算
class Solution:
    def maxA(self,N: int) -> int:
        self.memo = {}
        res = self.dp(N,0,0)
        print(self.memo)
        return res

    def dp(self,n,a_num,copy):
        if n <= 0:
            return a_num
        if (n,a_num,copy) in self.memo:
            return self.memo[(n,a_num,copy)]
        self.memo[(n,a_num,copy)] = max(
            self.dp(n-1,a_num+1,copy),    # A
            self.dp(n-1,a_num+copy,copy), # C-V
            self.dp(n-2,a_num,a_num)      # C-A C-C
        )
        return self.memo[(n,a_num,copy)]

#思路2 O(N^2)
#最优的序列应该是这种形式：A,A..C-A,C-C,C-V,C-V..C-A,C-C,C-V..
#状态只有1个：剩余按键次数n
#选择：最后一次是按A还是ctrl+v
#dp[n]代表n次操作后A的最多个数
#base case:dp[0] = 0
#状态转移 dp[n]=dp[n-1]+1 按A
#              dp[j-2]*(i-j+1) 在ctrl+A->ctrl+c后按若干次ctrl+v
class Solution:
    def maxA(self,N: int) -> int:
        dp = [0] * (N+1)
        for i in range(1,N+1):
            dp[i] = dp[i-1] + 1 #按 A 键
            for j in range(2,i+1):
                dp[i] = max(dp[i],dp[j-2]*(i-j+1)) #全选 & 复制 dp[j-2]，连续粘贴 i - j 次
        return dp[-1]

if __name__ == '__main__':
    N=7
    print(Solution().maxA(N))