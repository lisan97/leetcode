class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #两种情况：要么第一间房子抢最后一间不抢(nums[1:])；要么最后一间房子抢第一间不抢(nums[:n-1])。
        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[:2])
        if n == 3:
            return max(nums[:3])
        pre = nums[0]
        cur1 = max(nums[:2])
        for i in range(2,n-1):
            tmp = max(cur1,pre+nums[i])
            pre = cur1
            cur1 = tmp
        pre = nums[1]
        cur2 = max(nums[1:3])
        for i in range(3,n):
            tmp = max(cur2,pre+nums[i])
            pre = cur2
            cur2 = tmp
        return max(cur1,cur2)