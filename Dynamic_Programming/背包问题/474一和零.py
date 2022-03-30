class Solution(object):
    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        #状态：1.第i个str;2.z个0;3.o个1
        #选择：是否放入这个字符串
        #dp[i][z][o]表示前i个字符串，在允许有z个0，o个1的情况下的最大子集长度
        #base case:dp[0][:][:] = 0, dp[:][0][0] = 0
        #状态转移:dp[i][z][o] = max(dp[i-1][z][o],dp[i-1][z-zeros[i]][o-ones[i]]+len(strs[i]))
        from collections import defaultdict
        length = len(strs)
        zeros = []
        ones = []
        for i in range(length):
            zero,one = self.count(strs[i])
            zeros.append(zero)
            ones.append(one)
        dp = [[[0]*(n+1) for _ in range(m+1)] for _ in range(length+1)]
        for i in range(1,length+1):
            for z in range(0,m+1):
                for o in range(0,n+1):
                    if zeros[i-1] > z or ones[i-1] > o:
                        dp[i][z][o] = dp[i-1][z][o]
                    else:
                        dp[i][z][o] = max(dp[i-1][z][o],dp[i-1][z-zeros[i-1]][o-ones[i-1]]+1)
        return dp[-1][-1][-1]

#三维压缩成二维
class Solution(object):
    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        from collections import defaultdict
        dp = [[0]*(n+1) for _ in range(m+1)]
        for string in strs:
            count0,count1 = self.count(string)
            for i in range(m,count0-1,-1):
                for j in range(n,count1-1,-1):
                    dp[i][j] = max(dp[i][j],dp[i-count0][j-count1]+1)

        return dp[-1][-1]

    def count(self,str):
        dic = defaultdict(int)
        for c in str:
            dic[c] += 1
        return dic['0'],dic['1']