class Solution(object):
    def exchange(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        '''
        使用头尾双指针
        奇偶：不做操作，i+=1,j-=1
        奇奇：i+=1
        偶奇：交换两个数，i+=1,j-=1
        偶偶：j-=1
        '''
        n = len(nums)
        i = 0
        j = n - 1
        while j > i:
            if nums[i] % 2:
                if nums[j] % 2 == 0:
                    j -= 1
                i += 1
            else:
                if nums[j] % 2:
                    nums[i], nums[j] = nums[j] , nums[i]
                    i += 1
                j -= 1
        return nums