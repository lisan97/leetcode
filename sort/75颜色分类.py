#计数排序
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        count = [0]*3
        for num in nums:
            count[num] += 1
        i = 0
        for j in range(len(count)):
            while count[j] > 0:
                nums[i] = j
                count[j] -= 1
                i += 1
        return nums

#follow up一次遍历完成
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        #循环不变量
        # all in [0, p0) = 0
        # all in [p0, i) = 1
        # all in (p2, len - 1] = 2
        def swap(nums,index1,index2):
            nums[index1], nums[index2] = nums[index2], nums[index1]

        n = len(nums)
        p0 = 0
        i = 0
        p2 = n - 1
        while i <= p2:
            if nums[i] == 0:
                swap(nums,p0,i)
                p0 += 1
                i += 1
            elif nums[i] == 1:
                i += 1
            else:
                swap(nums,i,p2)
                p2 -= 1