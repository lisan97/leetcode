#O(n)
class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return -1
        #用nums的正负来记录该索引有没有出现过1
        for i in range(len(nums)):
            pos = abs(nums[i])
            if nums[pos] > len(nums):
                return -1
            if nums[pos] < 0:
                return pos
            #防止索引已经变负都要加abs
            nums[pos] = -nums[pos]
        return -1

#二分法 O(nlogn)
class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            count = self.countRange(nums,mid)
            #[left,mid]这段数量正常，则重复的在[mid,right]这段
            if count <= mid:
                left = mid + 1
            else:
                right = mid
        return left


    def countRange(self,nums,mid):
        count = 0
        for num in nums:
            if num <= mid:
                count += 1
        return count