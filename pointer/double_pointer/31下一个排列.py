class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        '''
        1.在尽可能靠右的低位进行交换，需要从后向前查找;如果没有找到，则说明没有比这大的排列了，那么直接跳过步骤2执行步骤3进行反转
        2.将一个 尽可能小的「大数」 与前面的「小数」交换
        3.将「大数」换到前面后，需要将「大数」后面的所有数重置为升序，升序排列就是最小的排列。
        '''
        n = len(nums)
        i = n - 2
        #1.寻找下一个数比前一个数大的组合
        while i >= 0 and nums[i] >= nums[i+1]:
            i -= 1
        #2.找到的话，再从后面找到尽可能小的比nums[i]大的那个数，然后交换两个数
        if i >= 0:
            j = n - 1
            #因为[i+1,n-1]这段是降序的，找到第一个比nums[i]大的就行
            while j >= i+1 and nums[i] >= nums[j]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
        #3.将nums[i+1:]升序排列，翻转一下就行，因为之前肯定是降序的
        right = n - 1
        left = i + 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1