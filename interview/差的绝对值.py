''' 
现在有个有序数组，想知道里面有多少对数的差的绝对值<=x
'''

def diffnum(nums,x):
    if not nums:
        return 0
    n = len(nums)
    i = 0
    j = 0
    res = 0
    while i < n:
        while j < n and (nums[j] - nums[i]) <= x:
            j += 1
        res += (j - i - 1)
        i += 1
    return res

if __name__ == '__main__':
    nums = [1,2,4,7,11,13]
    x = 2
    print(diffnum(nums,x))