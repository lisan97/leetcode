#动态规划
class Solution(object):
    def findLength(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        #状态i,j
        #dp[i][j]第一个数组截止到第i个，第二个数组截止到第j个的最长公共子数组的长度
        #base case:dp[0][0] = 1 if nums1[0] == nums2[0] else 0
        #状态转移:dp[i][j] = dp[i-1][j-1] + 1 if nums1[i] == nums2[j] else 0
        m = len(nums1)
        n = len(nums2)
        dp = [[0] * n for _ in range(m)]
        res = 0
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    dp[i][j] = 1 if nums1[i] == nums2[j] else 0
                else:
                    dp[i][j] = dp[i-1][j-1] + 1 if nums1[i] == nums2[j] else 0
                res = max(res,dp[i][j])
        return res

#滑动窗口
class Solution(object):
    def findLength(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        return self.findmax(nums1,nums2) if len(nums1) <= len(nums2) else self.findmax(nums2,nums1)

    def findmax(self,nums1,nums2):
        res = 0
        m = len(nums1)
        n = len(nums2)
        '''
        A:           |*|*|*|*|
        B: |*|*|*|*|*|*|
                 ↓
        A:       |*|*|*|*|
        B: |*|*|*|*|*|*|
        '''
        for length in range(1,m):
            res = max(res,self.maxlen(nums1,0,nums2,n-length,length))
        '''
        A:     |*|*|*|*|
        B: |*|*|*|*|*|*|
                 ↓
        A: |*|*|*|*|
        B: |*|*|*|*|*|*|
        '''
        for j in range(n-m,-1,-1):
            res = max(res,self.maxlen(nums1,0,nums2,j,m))
        '''
        A: |*|*|*|*|
        B:   |*|*|*|*|*|*|
                 ↓
        A: |*|*|*|*|
        B:       |*|*|*|*|*|*|
        '''
        for i in range(1,m):
            res = max(res,self.maxlen(nums1,i,nums2,0,m - i))
        return res

    def maxlen(self,nums1,i,nums2,j,length):
        count = 0
        res = 0
        for k in range(length):
            if nums1[i+k] == nums2[j+k]:
                count += 1
            else:
                if count > 0:
                    res = max(res, count)
                    count = 0
        return max(res,count)