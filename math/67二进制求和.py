class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        return str(bin(int(a,2)+int(b,2)))[2:]

#模拟列竖式
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        m = len(a)
        n = len(b)
        if m < n:
            m,n = n,m
            a,b = b,a
        i = m-1
        j = n-1
        res = []
        carry = 0
        while i>=0 and j>=0:
            t = int(a[i])+int(b[j])+carry
            if t >= 2:
                t -= 2
                carry = 1
            else:
                carry = 0
            res.append(str(t))
            i -= 1
            j -= 1
        while i>=0:
            t = int(a[i])+carry
            if t >= 2:
                t -= 2
                carry = 1
            else:
                carry = 0
            res.append(str(t))
            i -= 1
        if carry:
            res.append(str(carry))
        res.reverse()
        return ''.join(res)

if __name__ == '__main__':
    a = '11'
    b = '11'
    print(Solution().addBinary(a,b))