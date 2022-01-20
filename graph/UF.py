class UF(object):
    def __init__(self,n):
        self.count = n#连通分量个数
        self.parent, self.size = self.init(n)#记录树的「重量」;记录树的「重量」

    def init(self,n):
        parent = []
        size = []
        for i in range(n):
            parent.append(i)
            size.append(1)
        return parent, size

    #返回节点 x 的连通分量根节点
    def find(self,x):
        while self.parent[x] != x:
            #进行路径压缩，保证任意树的高度保持在常数，使得 union 和 connected API 时间复杂度为 O(1)。
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    #将节点 p 和节点 q 连通
    def union(self,p,q):
        rootP = self.find(p)
        rootQ = self.find(q)
        if rootP == rootQ:
            return
        #小树接到大树下面，较平衡
        if self.size[rootP] < self.size[rootQ]:
            self.parent[rootP] = rootQ
            self.size[rootQ] += self.size[rootP]
        else:
            self.parent[rootQ] = rootP
            self.size[rootP] += self.size[rootQ]
        #两个连通分量合并成一个连通分量
        self.count -= 1

    #判断节点 p 和节点 q 是否连通
    def connected(self,p,q):
        rootP = self.find(p)
        rootQ = self.find(q)
        return rootP == rootQ

    #返回图中的连通分量个数
    def Count(self):
        return self.count

