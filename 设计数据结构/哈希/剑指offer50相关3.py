'''
在英语中，如果两个单词中出现的字母相同，并且每个字母出现的次数也相同，那么这两个单词互为变位词。
那么请完成一个函数，判断输入的两个字符串是不是互为变位词
'''
class Solution(object):
    def firstUniqChar(self, a,b):
        if len(a) != len(b):
            return False
        arr = [0] * 26
        for i in range(len(a)):
            arr[ord(a[i])-ord('a')] += 1
            arr[ord(b[i]) - ord('a')] -= 1
        for i in range(len(arr)):
            if arr[i]:
                return False
        return True



if __name__ == '__main__':
    a = 'evil'
    b = 'live'
    print(Solution().firstUniqChar(a, b))