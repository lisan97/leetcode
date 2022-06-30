#找到所有峰的第一个索引
def find(nums):
    n = len(nums)
    if n < 3:
        return []
    res = []
    first = False #前一个小于现在，现在大于等于下一个
    index = -1
    for i in range(1,n):
        if not first:
            if i < n-1 and nums[i-1] < nums[i] and nums[i] >= nums[i+1]:
                first = True
                index = i
            else:
                continue
        else:
            if nums[i-1] > nums[i]:
                res.append(index)
                first = False
                index = -1
            else:
                continue
    return res

if __name__ == '__main__':
    nums = [1,2,1,2,2,1]
    #nums = [1,2,1]
    #nums = [1,3]
    #nums = [1,2,1,2,2,1]
    print(find(nums))