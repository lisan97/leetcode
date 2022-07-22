#小顶堆
#是一种特殊的二叉树（完全二叉树），只不过存储在数组里
#父节点： i / 2;左子节点： i * 2;右子节点：i * 2 + 1
class BinHeap:
	def __init__(self):
		self.heapList = [0] #索引 0 不用，所以多分配一个空间
		self.currentSize = 0

	def swim(self, i):
		#如果浮到堆顶，就不能再上浮了
		while i // 2 > 0 and self.heapList[i] < self.heapList[i//2]:
			#如果第 x 个元素比上层大
        	#将 x 换上去
			self.heapList[i//2], self.heapList[i] = self.heapList[i], self.heapList[i//2]
			i = i//2

	def insert(self, k):
		#先把新元素加到最后
		self.heapList.append(k)
		self.currentSize += 1
		#然后让它上浮到正确的位置
		self.swim(self.currentSize)

	def sink(self,i):
		stop = False
		while i*2 < self.currentSize and not stop:
			mid = self.midPoint(i) #选择左子节点里右子节点更小的去比
			if self.heapList[i] > self.heapList[mid]:
				self.heapList[mid], self.heapList[i] = self.heapList[i], self.heapList[mid]
			#结点 x 比俩孩子都小，就不必下沉了
			else:
				stop = True
			i = mid

	#选左右子节点更小的那个
	def midPoint(self,i):
		if i*2+1 > self.currentSize:
			return i*2
		else:
			if self.heapList[i*2] < self.heapList[i*2+1]:
				return i*2
			else:
				return i*2+1

	def delMin(self):
		#最大堆的堆顶就是最小元素
		delVal = self.heapList[1]
		#把这个最小元素换到最后，删除之
		self.heapList[1] = self.heapList[self.currentSize]
		self.currentSize -= 1
		self.heapList.pop()
		#让 pq[1] 下沉到正确位置
		self.sink(1)
		return delVal

	def buildHeap(self,lst):
		self.currentSize = len(lst)
		i = self.currentSize//2
		self.heapList = [0] + lst[:]
		while i>0:
			self.sink(i)
			i -= 1

if __name__ == '__main__':
	bh = BinHeap()
	bh.buildHeap([9, 5, 6, 2, 3])

	print(bh.delMin())
	print(bh.delMin())
	print(bh.delMin())
	print(bh.delMin())
	print(bh.delMin())