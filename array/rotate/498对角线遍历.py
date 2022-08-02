class Solution(object):
    def findDiagonalOrder(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """
        #up表示方向，超左上还是右下
        #(leftx,lefty)表示左边的边界
        #(upx,upy)表示上方的边界
        self.res = []
        m = len(mat)
        n = len(mat[0])
        up = True
        leftx,lefty,upx,upy = 0, 0, 0, 0
        total = m * n
        while len(self.res) < total:
            self.diawalk(mat,leftx,lefty,upx,upy,up)
            if leftx < m - 1:
                leftx += 1
            else:
                lefty += 1
            if upy < n - 1:
                upy += 1
            else:
                upx += 1
            up = not up
        return self.res

    def diawalk(self,mat,leftx,lefty,upx,upy,up):
        if up:
            while leftx >= upx:
                self.res.append(mat[leftx][lefty])
                leftx -= 1
                lefty += 1
        else:
            while upx <= leftx:
                self.res.append(mat[upx][upy])
                upx += 1
                upy -= 1