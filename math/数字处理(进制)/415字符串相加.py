class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        m = len(num1)
        n = len(num2)
        if m < n:
            m,n = n,m
            num1,num2 = num2,num1
        i = m-1
        j = n-1
        res = []
        carry = 0
        while i >= 0 and j >= 0:
            t = int(num1[i]) + int(num2[j]) + carry
            if t >= 10:
                t -= 10
                carry = 1
            else:
                carry = 0
            res.append(str(t))
            i -= 1
            j -= 1
        while i >= 0:
            t = int(num1[i]) + carry
            if t >= 10:
                t -= 10
                carry = 1
            else:
                carry = 0
            res.append(str(t))
            i -= 1
        #需注意还有没有进位数没加上去(例如：1,9)
        if carry:
            res.append(str(carry))
        res.reverse()
        return ''.join(res)

class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        m = len(num1)
        n = len(num2)
        i = m-1
        j = n-1
        carry = 0
        res = ''
        while i >= 0 or j >= 0:
            a = int(num1[i]) if i >= 0 else 0
            b = int(num2[j]) if j >= 0 else 0
            total = carry + a + b
            carry = total // 10
            exist = total % 10
            res = str(exist) + res
            i -= 1
            j -= 1
        if carry:
            res = '1' + res
        return res