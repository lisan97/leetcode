class Solution:
    def findContinuousSequence(self, target: int) -> List[List[int]]:
        res = []
        for n in range(target//2,1,-1):
            #n为奇数
            if n % 2:
                #n能被target整除
                if not target % n:
                    mid = target / n
                    i = int(mid) #双指针从中间往外扩散
                    j = int(mid)
                    num = int(n // 2) #需要扩散的次数
                    if i - num > 0:
                        res.append([a for a in range(i-num,j+num+1)])
                #n不能被target整除
                else:
                    continue
            #n为偶数
            else:
                mid = target / n
                str_mid = str(mid)
                #除得的结果是以0.5结尾
                if str_mid[-2] == '.' and str_mid[-1] == '5':
                    i = int(mid)
                    j = int(mid) + 1
                    num = int(n / 2 - 1)
                    if i - num > 0:
                        res.append([a for a in range(i-num,j+num+1)])
                else:
                    continue
        return res

class Solution:
    def findContinuousSequence(self, target: int) -> List[List[int]]:
        '''
        维护双指针，并记录指针内部的和cursum，
        若cursum > target，cursum - i，i往前移一位
        若cursum < target, j往前移一位, cursum + j
        若cursum = target，将[i,j]放入结果，j往前移一位,cursum+j
        '''
        res = []
        i = 1
        j = 2
        mid = target // 2 + 1
        cursum = i + j
        while i < mid:
            if cursum == target:
                res.append([n for n in range(i,j+1)])
                j += 1
                cursum += j
            elif cursum < target:
                j += 1
                cursum += j
            else:
                cursum -= i
                i += 1
        return res