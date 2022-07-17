#该题是leetcode 55. 跳跃游戏  的变形
''' 
从起点开始接下来有N个方块，相邻方块间的距离都为1，每个方块上有增加体力的食用蘑菇或减少体力的毒蘑菇，蘑菇带来的体力改变是已知的。
一个人初始体力为m，每次可以往前跳任意个方块，体力耗尽就会死掉。
每跳一次消耗的体力与跳的距离成正比，比例为1。
问这个人能否跳到终点，如果能，求可能剩余的最大体力。如果不行返回-1
'''

def mushroom(nums,m):
    end = 0
    nums = [m] + nums + [0]
    n = len(nums)
    for i in range(n):
        if i > end:
            return -1
        end = max(end,i+nums[i])
    return end - n + 1

if __name__ == '__main__':
    nums = [1,2,3,-2,5]
    m = 1
    print(mushroom(nums,m))