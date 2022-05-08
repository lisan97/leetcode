class Solution(object):
    def permutation(self, nums):
        '''
        输入一个含有8个数字的数组，判断有没有可能把这8个数字分别放到正方体的8个顶点上，
        使得正方体上三组相对面上的4个顶点的和都相等，即：
        a1+a2+a3+a4=a5+a6+a7+a8; a1+a3+a5+a7=a2+a4+a6+a8; a1+a2+a5+a6=a3+a4+a7+a8

        解法:相当于求出8个数字的全排列，然后判断有没有符合条件的
        '''
        used = [False] * 8
        self.found = False
        track = []
        self.traverse(nums,track,used)
        return self.found

    def traverse(self,nums,track,used):
        if self.found:
            return
        if len(track) == 8:
            if self.isValid(track):
                self.found = True
            return
        for i in range(8):
            if self.found:
                break
            if used[i]:
                continue
            track.append(nums[i])
            used[i] = True
            self.traverse(nums,track,used)
            track.pop()
            used[i] = False


    def isValid(self,track):
        if track[0] + track[1] + track[2] + track[3] != track[4] + track[5] + track[6] + track[7]:
            return False
        if track[0] + track[2] + track[4] + track[6] != track[1] + track[3] + track[5] + track[7]:
            return False
        if track[0] + track[1] + track[4] + track[5] != track[2] + track[3] + track[6] + track[7]:
            return False
        return True