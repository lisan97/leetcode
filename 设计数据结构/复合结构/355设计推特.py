class Tweet(object):
    def __init__(self,id,time):
        #推文内容（id）和发文时间
        self.id = id
        self.time = time
        self.next = None

class User(object):
    def __init__(self,userId):
        self.followed = set()
        self.id = userId
        #用户发表的推文链表头结点
        self.head = None
        #关注一下自己
        self.follow(userId)

    def follow(self, userId):
        self.followed.add(userId)

    def unfollow(self,userId):
        #不可以取关自己
        if userId != self.id and userId in self.followed:
            self.followed.remove(userId)

    def post(self,tweetId,timestamp):
        twt = Tweet(tweetId,timestamp)
        #将新建的推文插入链表头
        #越靠前的推文 time 值越大
        twt.next = self.head
        self.head = twt
from heapq import *
class Twitter(object):

    def __init__(self):
        self.timestamp=0
        self.userMap = {}


    def postTweet(self, userId, tweetId):
        """
        :type userId: int
        :type tweetId: int
        :rtype: None
        """
        if userId not in self.userMap:
            self.userMap[userId] = User(userId)
        u = self.userMap[userId]
        u.post(tweetId,self.timestamp)
        self.timestamp += 1


    def getNewsFeed(self, userId):
        """
        :type userId: int
        :rtype: List[int]
        """
        res = []
        if userId not in self.userMap:
            return res
        users = self.userMap[userId].followed
        pq = []
        for id in users:
            twt = self.userMap[id].head
            while twt:
                pq.append(twt)
                twt = twt.next
        return [twt.id for twt in nlargest(10, pq, key=lambda twt: twt.time)]

    def follow(self, followerId, followeeId):
        """
        :type followerId: int
        :type followeeId: int
        :rtype: None
        """
        if followerId not in self.userMap:
            u = User(followerId)
            self.userMap[followerId] = u

        if followeeId not in self.userMap:
            u = User(followeeId)
            self.userMap[followeeId] = u

        self.userMap[followerId].follow(followeeId)


    def unfollow(self, followerId, followeeId):
        """
        :type followerId: int
        :type followeeId: int
        :rtype: None
        """
        if self.userMap[followerId]:
            flwer = self.userMap[followerId]
            flwer.unfollow(followeeId)