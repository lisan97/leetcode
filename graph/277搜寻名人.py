#可以直接调用，能够返回 i 是否认识 j
def knows(i, j):
    pass

class Solution(object):
    def findCelebrity(self,n):
        #先假设 cand 是名人
        can = 0
        for other in range(1,n):
            if knows(can,other) or not knows(other,can):
                #cand 不可能是名人，排除
                #假设 other 是名人
                can = other
            #否则other不可能是名人，排除
            #什么都不用做，继续假设cand是名人
        #现在的 cand 是排除的最后结果，但不能保证一定是名人
        for other in range(n):
            if can == other:
                continue
            #需要保证其他人都认识 cand，且 cand 不认识任何其他人
            if knows(can,other) or not knows(other,can):
                return -1
        return can