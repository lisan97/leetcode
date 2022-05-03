class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        #先去掉首尾空格并小写
        s = s.strip().lower()
        '''
        数字
        字符串，只能是e,e前面得是数字或小数点,且e后面得是+/-或数字，而且得是整数
        +/-出现时，要么是第一个，且后面得跟数字；要么是e的后面一个且其后面必须有数字，而且得是整数
        .前面或后面至少得有数字，而且.只能出现一次
        '''
        if not s:
            return False
        for i,c in enumerate(s):
            #数字
            if c.isdigit():
                continue
            #为e，不是第一个，不是最后一个，前一个是数字或.
            elif c.isalpha() and c == 'e' and i != 0 and (s[i-1].isdigit() or s[i-1] == '.') and len(s) > i+1:
                #后一个为+/-时，不是最后一个，剩余的得是整数
                if s[i+1] in ['+','-'] and len(s) > i+2 and s[i+2:].isdigit():
                    return True
                #剩余的都是整数
                elif s[i+1:].isdigit():
                    return True
                else:
                    return False
            #在e后面的情况上面已经考虑了，所以只可能是处于第一个的情况
            elif c in ['+','-'] and i == 0 and len(s) > 1:
                #下一个得是数字或.
                if s[i+1].isdigit() or s[i+1] == '.':
                    continue
                else:
                    return False
            #为.
            elif c == '.':
                #后面还出现.
                if '.' in set(s[i+1:]):
                    return False
                #不是第一个，前一个是数字
                elif i != 0 and s[i-1].isdigit():
                    continue
                #不是最后一个，后一个为数字
                elif len(s) > i + 1 and s[i+1].isdigit():
                    continue
                else:
                    return False
            else:
                return False
        return True
