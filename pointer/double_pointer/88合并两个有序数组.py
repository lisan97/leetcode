class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        '''
        可以把两个指针分别放在两个数组的末尾，每次将较大的那个数字复制到 nums1 的后边，然后向前移动一位
        如果 nums1的数字已经复制完，不要忘记把 nums2 的数字继续复制；
        如果 nums2 的数字已经复制完，剩余nums1 的数字不需要改变，因为它们已经被排好序
        '''
        i = m-1
        j = n-1
        pos = m+n-1
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[pos] = nums1[i]
                i -= 1
            else:
                nums1[pos] = nums2[j]
                j -= 1
            pos -= 1
        while j >= 0:
            nums1[pos] = nums2[j]
            j -= 1
            pos -= 1