'''
一维消消乐问题：大于等于四个连续相同数字可以消除 nums=[1 1 1 0 0 0 0 0 1 2 2 3 3 3 3]的结果为[2 2]
'''

def func(nums):
    from collections import defaultdict
    dic = defaultdict(int)
    res = []
    for num in nums:
        dic[num] += 1
    for num in nums:
        if dic[num] < 4:
            res.append(num)
    return res

if __name__ == '__main__':
    nums = [1 ,1 ,1 ,0, 0, 0 ,0, 0, 1, 2, 2, 3, 3, 3 ,3]
    print(func(nums))