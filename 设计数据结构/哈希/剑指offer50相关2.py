'''
定义一个函数，删除字符中所有重复出现的字符
'''
class Solution(object):
    def firstUniqChar(self, a):
        arr = [False] * 256
        i = 0
        res = []
        for c in a:
            if not arr[ord(c)]:
                res.append(c)
                arr[ord(c)] = True
        return ''.join(res)


if __name__ == '__main__':
    s = "google"
    print(Solution().firstUniqChar(s))