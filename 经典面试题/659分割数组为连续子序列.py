class Solution(object):
    def isPossible(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        #1.跟在别的子序列后面(need[i]>0) 优先考虑
        #2.以自己为开头成立一个子序列 后面得起码有俩连续的(freq[i+1]>0, freq[i+2]>0)
        from collections import defaultdict
        freq = defaultdict(int)
        need = defaultdict(int)
        for n in nums:
            freq[n] += 1
        for n in nums:
            #已经被别的序列使用
            if freq[n] == 0:
                continue
            #跟在别的子序列后面
            elif need[n] > 0:
                freq[n] -= 1
                need[n] -= 1 #对 n 的需求减一
                need[n+1] += 1 #对 n + 1 的需求加一
            #以自己为开头成立一个子序列
            elif freq[n] > 0 and freq[n+1] > 0 and freq[n+2] > 0:
                #将 n 作为开头，新建一个长度为 3 的子序列 [n,n+1,n+2]
                freq[n] -= 1
                freq[n+1] -= 1
                freq[n+2] -= 1
                need[n+3] += 1 #对 n + 3 的需求加一
            #两种情况都不符合，则无法分配
            else:
                return False
        return True

'''
follow up:想要你给我把子序列都打印出来，怎么办？
其实这也很好实现，只要修改 need，不仅记录对某个元素的需求个数，而且记录具体是哪些子序列产生的需求
'''