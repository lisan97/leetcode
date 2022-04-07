# def rand7():
# @return a random integer in the range 1 to 7

class Solution(object):
    def rand10(self):
        """
        :rtype: int
        """
        while True:
            num = (rand7() - 1) * 7 + rand7() #rand 49
            #拒绝采样
            if num <= 40:
                return num % 10 + 1
            #利用这些范围外的数字，以减少丢弃的值，提高命中率总而提高随机数生成效率
            num = (num-40-1) * 7 + rand7()
            if num <= 60:
                return num % 10 + 1
            num = (num-60-1) * 7 + rand7() #rand 63
            if num <= 20:
                return num % 10 + 1 #rand 21