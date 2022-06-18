class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        '''
        我们仍然可以利用这个数组的递增性，使用二分查找。
        对于当前的中点，如果它指向的值小于等于右端，那么说明右区间是排好序的；
        反之，那么说明左区间是排好序的。
        如果目标值位于排好序的区间内，我们可以对这个区间继续二分查找；
        反之，我们对于另一半区间继续二分查找。
        '''
        n = len(nums)
        left = 0
        right = n - 1
        while left <= right:
            mid = (right-left)//2+left
            if nums[mid] == target:
                return True
            if nums[mid] == nums[left]:
                #无法判断哪个区间是增序的
                left += 1
            elif nums[mid] <= nums[right]:
                #右边为递增区间
                if target > nums[mid] and target <= nums[right]:
                    left = mid + 1
                else:
                    #不符合条件两种情况：
                    #1.target比nums[mid]小
                    #2.target大于nums[right]
                    #这两种情况都要去左区间查找
                    right = mid - 1
            else:
                #左边为递增区间
                if target < nums[mid] and target > nums[right]:
                    right = mid - 1
                else:
                    #不符合条件两种情况：
                    #1.target比nums[mid]大
                    #2.target小于nums[left]
                    #这两种情况都要去右区间查找
                    left = mid + 1
        return False