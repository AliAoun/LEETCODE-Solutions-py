class Twitter:

    def __init__(self):
        self.count=0
        self.following=defaultdict(set)
        self.post=defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.post[userId].append([self.count,tweetId])
        self.count-=1

    def getNewsFeed(self, userId: int) -> List[int]:
        self.following[userId].add(userId)
        minHeap=[]
        for followee in self.following[userId]:
            i=len(self.post[followee])-1
            if i>=0:
                count,tweetId=self.post[followee][i]
                minHeap.append([count,tweetId,followee,i])
        heapq.heapify(minHeap)
        res=[]

        while minHeap and len(res)<10:
            count,tweetId,followee,index=heapq.heappop(minHeap)
            res.append(tweetId)
            if index>0:
                count,tweetId=self.post[followee][index-1]
                heapq.heappush(minHeap, [count,tweetId,followee,index-1])
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)


# Overall Time Complexity:# - postTweet: O(1)
# - getNewsFeed: O(N log k), where N is the total number of tweets from followed users and k is the number of followed users.# - follow: O(1)
# - unfollow: O(1) 
# Overall Space Complexity: O(U + T), where U is the number of users and T is the total number of tweets.
