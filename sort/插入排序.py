class Solution:
    def sortArray(self, nums: list) -> list:
        n = len(nums)
        for i in range(1,n):
            pos = i
            tmp = nums[i]
            while pos > 0 and tmp < nums[pos-1]:
                nums[pos] = nums[pos-1]
                pos -= 1
            nums[pos] = tmp
        return nums

if __name__ == '__main__':
    nums = [5,1,1,2,0,0]
    print(Solution().sortArray(nums))