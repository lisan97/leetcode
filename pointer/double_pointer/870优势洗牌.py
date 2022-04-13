#双指针+优先队列O(nlogn)
class Solution(object):
    def advantageCount(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        '''
        用优先队列保存nums2，使得nums2也是顺序了，这样只要每次拿nums2最大的和nums1最大的比就行，
        不需要循环nums2里的每个数，去nums1里做二分查找
        '''
        from heapq import *
        #给num1升序排列
        nums1.sort()
        pq = []
        #给 nums2 降序排序，并保存之前的索引
        for i,v in enumerate(nums2):
            heappush(pq,(-v,i))
        #nums1[left] 是最小值，nums1[right] 是最大值
        left,right = 0, len(nums1) - 1
        res = [0] * len(nums1)
        while pq:
            val,i = heappop(pq)
            #如果 nums1[right] 能胜过 val，那就自己上
            if nums1[right] > -val:
                res[i] = nums1[right]
                right -= 1
            else:
                #否则用最小值去送人头
                res[i] = nums1[left]
                left += 1
        return res

#二分查找也能过，但时间复杂度比上面要高O(n²logn)
class Solution(object):
    def advantageCount(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        #思路：田忌赛马，如果nums2中的一个数，nums1有比它大的，则用比它大的数里面最小的那个战胜他；
        #如果没有比它大的，则用最小的那个数输给他
        nums1.sort()
        res = []
        for num in nums2:
            left = self.leftbound(nums1,num)
            if left == len(nums1):
                left = 0
            res.append(nums1[left])
            del nums1[left]
        return res

    #求大于target的最小值
    def leftbound(self,nums,target):
        left = 0
        right = len(nums)
        while left < right:
            mid = (left+right)//2
            #求大于target的最小值，所以这里去<=，求大于等于target的最小值时用<
            if nums[mid] <= target:
                left = mid + 1
            else:
                right = mid
        return left