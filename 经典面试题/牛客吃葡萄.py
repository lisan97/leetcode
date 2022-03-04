n = int(input())
nums = [[int(num) for num in input().split()] for _ in range(n)]

for num in nums:
    num.sort()
    a,b,c = num[0],num[1],num[2]
    #能够构成三角形，可完全平分 或 不能构成三角形，但依然可以完全平分的情况
    if c <= 2*(a+b):
        print((a+b+c+2)//3)
    #不能构成三角形，平分最长边的情况
    else:
        print((c+1)//2)