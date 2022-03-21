class Solution:
    def sortArray(self, nums: list) -> list:
        n = len(nums)
        #先给辅助数组开辟内存空间
        self.temp = [0]*n
        #排序整个数组（原地修改）
        self.sort(nums,0,n-1)
        return nums

    #定义：将子数组 nums[l..h] 进行排序
    def sort(self,nums,l,h):
        #base case:单个元素不用排序
        if l == h:
            return
        mid = (h - l)//2+l
        #先对左半部分数组 nums[l..mid] 排序
        self.sort(nums,l,mid)
        #再对右半部分数组 nums[mid+1..h] 排序
        self.sort(nums,mid+1,h)
        #将两部分有序数组合并成一个有序数组
        self.merge(nums,l,mid,h)

    #定义:将 nums[l..mid] 和 nums[mid+1..h]这两个有序数组合并成一个有序数组
    def merge(self,nums,l,mid,h):
        #先把 nums[lo..hi] 复制到辅助数组中
        #以便合并后的结果能够直接存入 nums
        for i in range(l,h+1):
            self.temp[i] = nums[i]
        #数组双指针技巧，合并两个有序数组
        i = l
        j = mid + 1
        for p in range(l,h+1):
            #左半边数组已全部被合并
            if i == mid + 1:
                nums[p] = self.temp[j]
                j += 1
            #右半边数组已全部被合并
            elif j == h + 1:
                nums[p] = self.temp[i]
                i += 1
            elif self.temp[i] > self.temp[j]:
                nums[p] = self.temp[j]
                j += 1
            else:
                nums[p] = self.temp[i]
                i += 1