class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        ''' 
        直接记录下有几个 preSum[j] 和 preSum[i] - k 相等，直接更新结果，就避免了内层的 for 循环(计算preSum[i]-preSum[j]=k)
        在我们遍历到位置 i 时，假设当前的前缀和是 psum，那么dic[psum-k]即为以当前位置结尾、满足条件的区间个数，并更新全局的count
        '''
        #记录该前缀和出现的次数
        #base case
        from collections import defaultdict
        prenum = defaultdict(int)
        prenum[0] = 1
        res,sum0_i = 0,0
        for i in range(len(nums)):
            sum0_i += nums[i]
            #这是我们想找的前缀和 nums[0..j]
            sum0_j = sum0_i - k
            #如果前面有这个前缀和，则直接更新答案
            res += prenum[sum0_j]
            #把前缀和 nums[0..i] 加入并记录出现次数
            prenum[sum0_i] = prenum[sum0_i] + 1
        return res