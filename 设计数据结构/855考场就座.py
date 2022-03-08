class ExamRoom(object):

    def __init__(self, n):
        """
        :type n: int
        """
        self.n = n
        self.students = []

    def seat(self):
        """
        :rtype: int
        """
        if not self.students:
            student = 0

        else:
            # 从将student放在0上开始考虑,此时离最左的distance就是self.students[0]
            dist = self.students[0]
            student = 0
            for i, s in enumerate(self.students):
                if i:
                    # 计算相邻两个student的距离，如果大于现有最大距离就更新
                    prev = self.students[i - 1]
                    d = (s - prev) // 2
                    if d > dist:
                        dist = d
                        student = prev + d
            # 最后考虑一下将student放在n-1的位置的情况
            d = self.n - 1 - self.students[-1]
            if d > dist:
                student = self.n - 1
        # 将学生插入到已排序的座位列表
        bisect.insort(self.students, student)
        return student

    def leave(self, p):
        """
        :type p: int
        :rtype: None
        """
        try:
            self.students.remove(p)
        except:
            return