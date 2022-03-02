class Solution(object):
    def __init__(self):
        #备忘录避免重复计算
        self.memo = {}
    def diffWaysToCompute(self, expression):
        """
        :type expression: str
        :rtype: List[int]
        """
        if expression in self.memo:
            return self.memo[expression]
        res = []
        for i in range(len(expression)):
            c = expression[i]
            #扫描算式 input 中的运算符
            if c in ['+','-','*']:
                #以运算符为中心，分割成两个字符串，分别递归计算
                left = self.diffWaysToCompute(expression[:i])
                right = self.diffWaysToCompute(expression[i+1:])
                #通过子问题的结果，合成原问题的结果
                for a in left:
                    for b in right:
                        if c == '+':
                            res.append(a+b)
                        elif c == '-':
                            res.append(a-b)
                        else:
                            res.append(a*b)
        #base case：如果 res 为空，说明算式是一个数字，没有运算符
        if not res:
            res.append(int(expression))
        self.memo[expression] = res
        return res