class Solution(object):
    def maxSumTwoNoOverlap(self, nums, firstLen, secondLen):
        """
        :type nums: List[int]
        :type firstLen: int
        :type secondLen: int
        :rtype: int
        """
        #构造一个前缀和数组
        #两种情况：1.L在左,M在右，维护一个Lmax；2.M在左，L在右，维护一个Mmax
        n = len(nums)
        for i in range(1,n):
            nums[i] = nums[i-1] + nums[i]
        Lmax = nums[firstLen-1]
        Mmax = nums[secondLen-1]
        res = nums[firstLen+secondLen-1]
        for i in range(firstLen+secondLen,n):
            #L在左的情况
            Lmax = max(Lmax,nums[i-secondLen] - nums[i-secondLen-firstLen])
            ans1 = Lmax + nums[i] - nums[i-secondLen]
            #M在左的情况
            Mmax = max(Mmax,nums[i-firstLen] - nums[i-secondLen-firstLen])
            ans2 = Mmax + nums[i] - nums[i-firstLen]
            res = max(res,ans1,ans2)
        return res