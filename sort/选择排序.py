class Solution:
    def sortArray(self, nums: list) -> list:
        n = len(nums)
        #每一轮从待排序的记录中选出最小的元素，存放在序列的起始位置
        for i in range(n):
            pos = i
            for j in range(i+1,n):
                if nums[pos] > nums[j]:
                    pos = j
            tmp = nums[pos]
            nums[pos] = nums[i]
            nums[i] = tmp
        return nums

if __name__ == '__main__':
    nums = [5,1,1,2,0,0]
    print(Solution().sortArray(nums))