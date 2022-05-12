'''
定义一个函数，输入两个字符串，从第一个字符串中删除第二个字符串出现过的所有字符
'''
class Solution(object):
    def firstUniqChar(self, a,b):
        arr = [False] * 256
        for c in b:
            arr[ord(c)-ord('a')] = True
        res = []
        for c in a:
            if not arr[ord(c)-ord('a')]:
                res.append(c)
        return ''.join(res)

if __name__ == '__main__':
    a = "We are students"
    b = 'aeiou'
    print(Solution().firstUniqChar(a,b))
