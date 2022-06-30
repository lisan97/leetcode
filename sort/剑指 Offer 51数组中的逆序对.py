class Solution(object):
    def reversePairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #使用归并排序，当右边部分当前数比左边部分当前值小时，拿mid-i+1得到逆序对的数量（左边部分比当前数大的数的数量），因为左右都是顺序的
        if not nums:
            return 0
        n = len(nums)
        self.res = 0
        self.tmp = [0] * n
        self.sort(nums,0,n-1)
        return self.res

    def sort(self,nums,l,h):
        if l == h:
            return
        mid = (l+h) // 2
        self.sort(nums,l,mid) #使左边部分有序
        self.sort(nums,mid+1,h) #使右边部分有序
        self.merge(nums,l,mid,h) #将这两部分合并为有序数组

    def merge(self,nums,l,mid,h):
        self.tmp[l:h+1] = nums[l:h+1]
        i = l
        j = mid + 1
        for p in range(l,h+1):
            if i == mid + 1:#左边部分已经插入完毕
                nums[p] = self.tmp[j]
                j += 1
            elif j == h+1: #右边部分已经插入完毕
                nums[p] = self.tmp[i]
                i += 1
            elif self.tmp[i] > self.tmp[j]: #左边部分当前数比右边部分当前数大
                nums[p] = self.tmp[j]
                self.res += mid - i + 1
                j += 1
            else:
                nums[p] = self.tmp[i]
                i += 1