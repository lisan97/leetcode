class Solution(object):
    def advantageCount(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
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