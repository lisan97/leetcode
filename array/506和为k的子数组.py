class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        #记录该前缀和出现的次数
        #base case
        prenum = {0:1}
        res,sum0_i = 0,0
        for i in range(len(nums)):
            sum0_i += nums[i]
            #这是我们想找的前缀和 nums[0..j]
            sum0_j = sum0_i - k
            #如果前面有这个前缀和，则直接更新答案
            if sum0_j in prenum:
                res += prenum[sum0_j]
            #把前缀和 nums[0..i] 加入并记录出现次数
            prenum[sum0_i] = prenum.get(sum0_i,0) + 1
        return res