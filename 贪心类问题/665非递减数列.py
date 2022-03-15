class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        '''
        当出现nums[i] > nums[i+1]时，要么nums[i] = nums[i+1]，要么nums[i+1]=nums[i]，
        应该优先选择nums[i] = nums[i+1]，因为前面的序列已经符合要求了，而nums[i+1]后面的元素是啥我们还不知道呢，少动它为妙
        分三种情况处理
        '''
        n = len(nums)
        if n == 1:
            return True
        count = 0
        for i in range(n-1):
            if nums[i] > nums[i+1]:
                count += 1
                if count > 1:
                    return False
                #i=1,无nums[i-1]，应该优先选择nums[i] = nums[i+1]
                if i==0:
                    nums[i] = nums[i+1]
                #nums[i-1] <= nums[i+1]，应该优先选择nums[i] = nums[i+1]
                elif i > 0 and nums[i-1] <= nums[i+1]:
                    nums[i] = nums[i+1]
                #nums[i-1] > nums[i+1]，那只能修改nums[i+1] = nums[i]
                else:
                    nums[i+1] = nums[i]
        return True