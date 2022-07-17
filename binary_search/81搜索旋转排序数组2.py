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
                #[mid,right]为递增区间，并且target也在这段区间中
                if target > nums[mid] and target <= nums[right]:
                    left = mid + 1
                else:
                    #不符合条件两种情况：
                    #1.target比nums[mid]小
                    #2.target大于nums[right]
                    #这两种情况都要去左区间查找
                    right = mid - 1
            else:
                #[left,mid]为递增区间，并且target也在这段区间中
                if target < nums[mid] and target > nums[right]:
                    right = mid - 1
                else:
                    #不符合条件两种情况：
                    #1.target比nums[mid]大
                    #2.target小于nums[left]
                    #这两种情况都要去右区间查找
                    left = mid + 1
        return False

#详细版
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        n = len(nums)
        left = 0
        right = n - 1
        while left <= right:
            mid = (left+right) // 2
            if nums[mid] == target or nums[right] == target:
                return True
            #mid和right一样大，无法判定在哪一段，挪一格right再比
            if nums[mid] == nums[right]:
                right -= 1
            #mid比right小，说明mid在右半段
            elif nums[mid] < nums[right]:
                #mid比target小
                if nums[mid] < target:
                    #target比right小，说明target在[mid,right]这段
                    if target < nums[right]:
                        left = mid + 1
                    #target比right大，说明target在[left,mid]这段
                    else:
                        right = mid - 1
                #mid比target大，那target一定也比right小，在[left,mid]这段
                else:
                    right = mid - 1
            #mid比right大，说明mid在左半段
            else:
                #mid比target小，那target肯定也比right大,说明target在[mid,right]这段
                if nums[mid] < target:
                    left = mid + 1
                #mid比target大
                else:
                    #target比right小，说明target在[mid,right]这段
                    if target < nums[right]:
                        left = mid + 1
                    #target比right大，说明target在[left,mid]这段
                    else:
                        right = mid - 1
        return False