class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        m = len(num1)
        n = len(num2)
        #结果最多为 m + n 位数
        res = [0] * (m+n)
        #从个位数开始逐位相乘
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                mat = int(num1[i]) * int(num2[j])
                #乘积在 res 对应的索引位置
                p1 = i+j
                p2 = i+j+1
                #叠加到 res 上
                total = mat + res[p2]
                res[p2] = total % 10
                res[p1] += total // 10
        #结果前缀可能存的 0（未使用的位）
        i = 0
        while i < (m+n) and res[i] == 0:
            i += 1
        #将计算结果转化成字符串
        text = ''
        for j in range(i,(m+n)):
            text += str(res[j])
        return text if text else "0"