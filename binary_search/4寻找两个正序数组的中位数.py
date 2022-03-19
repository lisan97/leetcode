#时间O(m+n)，空间O(m+n)
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        res = []
        m = len(nums1)
        n = len(nums2)
        i = 0
        j = 0
        while i < m and j < n:
            if nums1[i] < nums2[j]:
                res.append(nums1[i])
                i += 1
            else:
                res.append(nums2[j])
                j += 1
        if i < m:
            for x in range(i,m):
                res.append(nums1[x])
        if j < n:
            for x in range(j,n):
                res.append(nums2[x])
        x = (m+n)//2
        return res[x] if (m+n)%2==1 else (res[x]+res[x-1])/2.0

#时间o(log(m+n)),空间复杂度o(1)
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m = len(nums1)
        n = len(nums2)
        left = (m+n+1)//2
        right = (m+n+2)//2
        #将偶数和奇数的情况合并，如果是奇数，会求两次同样的 k 。
        return (self.getKth(nums1,0,m-1,nums2,0,n-1,left)+self.getKth(nums1,0,m-1,nums2,0,n-1,right))*0.5

    def getKth(self,nums1,start1,end1,nums2,start2,end2,k):
        len1 = end1 - start1 + 1
        len2 = end2 - start2 + 1
        #当len1大于len2时交换两个数组，这样就能保证如果有数组空了，一定是 len1
        if len1 > len2:
            return self.getKth(nums2,start2,end2,nums1,start1,end1,k)
        #base case1 len1==0直接返回另一个数组第k个数
        if len1 == 0:
            return nums2[start2+k-1]
        #base case2 k==1直接取min(nums1[start1],nums2[start2])
        if k == 1:
            return min(nums1[start1],nums2[start2])
        #防止k//2超过数组长度的情况
        index1 = start1+min(k//2,len1) - 1
        index2 = start2+min(k//2,len2) - 1
        #如果nums2[k//2]比nums1[k//2]小，就表明nums2的前 k//2 个数字都不是第 k 小数字，所以可以排除,更新start2和k
        if nums1[index1] > nums2[index2]:
            return self.getKth(nums1,start1,end1,nums2,index2+1,end2,k - (index2-start2+1))
        else:
            return self.getKth(nums1,index1+1,end1,nums2,start2,end2,k - (index1-start1+1))