class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        #按照h降序并按照k升序，这样一个人前面的人数，就是身高>=他的数量，按照k降序排列可以减少插入次数
        n = len(people)
        if n == 1:
            return people
        people.sort(key=lambda x:(-x[0],x[1]))
        res = []
        for p in people:
            if len(res) <= p[1]:
                res.append(p)
            else:
                res.insert(p[1],p)
        return res

#原地修改
class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        #根据身高倒序排序后，i是多少就代表前面有几个人比他身高高；再按照x[1]排序是为了减少插入次数
        n = len(people)
        if n == 1:
            return people
        people.sort(key=lambda x:(-x[0],x[1]))
        i = 0
        while i < n:
            p = people[i]
            if i > p[1]:
                people.insert(p[1],p)
                people.pop(i+1)
            i+=1
        return people