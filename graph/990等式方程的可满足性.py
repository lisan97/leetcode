from UF import UF
class Solution(object):
    def equationsPossible(self, equations):
        """
        :type equations: List[str]
        :rtype: bool
        """
        #26 个英文字母
        uf = UF(26)
        base = ord('a')
        #先让相等的字母形成连通分量
        for eq in equations:
            if eq[1] == '=':
                x = ord(eq[0]) - base
                y = ord(eq[3]) - base
                uf.union(x,y)
        #检查不等关系是否打破相等关系的连通性
        for eq in equations:
            if eq[1] == '!':
                x = ord(eq[0]) - base
                y = ord(eq[3]) - base
                #如果相等关系成立，就是逻辑冲突
                if uf.connected(x,y):
                    return False
        return True