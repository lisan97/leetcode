'''
如果a和b的长度不一样，直接返回False。生成一个大字符串c，c是两个字符串a拼在一起的结果，即c = a + a，只要判断b是否为c的子串即可。
'''


def isRotation(str1, str2):
    if str1 == None or str2 == None or len(str1) != len(str2):
        return False

    str2 = str2 + str2

    return str1 in str2

