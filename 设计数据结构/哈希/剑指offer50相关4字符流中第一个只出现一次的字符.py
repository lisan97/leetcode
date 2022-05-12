'''
实现一个函数，用来找出字符流中第一个只出现一次的字符
意味着只能遍历一遍
'''

class Solution(object):
    def firstUniqChar(self, s):
        from collections import OrderedDict
        dic = OrderedDict()
        for c in s:
            if c not in dic:
                dic[c] = 1
            else:
                dic[c] += 1
        for k,v in dic.items():
            if v == 1:
                return k
        return ' '