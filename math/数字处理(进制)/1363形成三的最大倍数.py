#回溯，会超时
class Solution(object):
    def largestMultipleOfThree(self, digits):
        """
        :type digits: List[int]
        :rtype: str
        """
        # 组合，选择能被3整除的数量最多的组合，然后从大到小排
        track = []
        self.n = len(digits)
        self.res = -1
        self.maxlen = 0
        self.backtrack(digits, track, 0)
        return str(self.res) if self.res != -1 else ''

    def backtrack(self, digits, track, start):
        if self.isValid(track) and len(track) >= self.maxlen:
            num = ''.join([str(i) for i in sorted(track, reverse=True)])
            j = 0
            length = len(num)
            while j < length - 1 and num[j] == '0':
                j += 1
            self.res = max(self.res, int(num[j:]))
            self.maxlen = max(self.maxlen, len(track))
        for i in range(start, self.n):
            track.append(digits[i])
            self.backtrack(digits, track, i + 1)
            track.pop()

    def isValid(self, nums):
        if not nums:
            return False
        return not sum(nums) % 3

'''
如果取模3
等于0，那其实可以都要
如果是1，那就得去掉一个1或者两个2
如果是2那就得去掉一个2或者两个1.
'''
class Solution(object):
    def largestMultipleOfThree(self, digits):
        """
        :type digits: List[int]
        :rtype: str
        """
        n = len(digits)
        cnt = [0] * 10 #记录每个数出现的次数
        cmod = [0] * 3 #记录每个余数出现的次数
        total = 0
        for i in range(n):
            cnt[digits[i]] += 1
            cmod[digits[i] % 3] += 1
            total += digits[i]
        remove_mod = 0 #要删的余数
        remove_num = 0 #要删的数量
        mod = total % 3
        if mod == 1:
            if cmod[1] > 0:
                remove_mod = 1
                remove_num = 1
            else:
                remove_mod = 2
                remove_num = 2
        elif mod == 2:
            if cmod[2] > 0:
                remove_mod = 2
                remove_num = 1
            else:
                remove_mod = 1
                remove_num = 2
        ans = ''
        for i in range(10):
            for j in range(cnt[i]):
                if remove_num > 0 and i % 3 == remove_mod:
                    cnt[i] -= 1
                    remove_num -= 1
                else:
                    ans = str(i) + ans
        if len(ans) > 0 and ans[0] == "0":
            ans = "0"
        return ans