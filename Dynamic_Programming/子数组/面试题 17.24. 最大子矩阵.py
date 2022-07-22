class Solution(object):
    def getMaxMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        #将二维数组按列求和转化为一维数组，然后求最大子数组和
        m = len(matrix)
        n = len(matrix[0])
        ans = [0] * 4 #保存最大子矩阵的左上角和右下角的行列坐标
        maxsum = float('-inf') #记录最大值
        beginy = 0 #暂时记录左上角的列坐标
        for i in range(m): #以i为上边，从上而下扫描
            pre = [0] * n #重置一维数组
            for j in range(i,m,1):
                total = 0
                #相当于求一次最大子数组和
                for k in range(n):
                    pre[k] += matrix[j][k]
                    if total > 0:
                        total += pre[k]
                    #自立门户，暂时保存其左上角
                    else:
                        total = pre[k]
                        beginy = k
                    #更新答案
                    if total > maxsum:
                        maxsum = total
                        ans[0] = i
                        ans[1] = beginy
                        ans[2] = j
                        ans[3] = k
        return ans