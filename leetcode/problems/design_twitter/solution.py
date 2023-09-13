class Twitter:

    def __init__(self):
        self.followers = defaultdict(set)
        self.tweets = defaultdict(list)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append([self.time, tweetId])
        self.time -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        recentTweets = []
        heap = []
        self.followers[userId].add(userId)
        for user in self.followers[userId]:
            for post in self.tweets[user][::-1]:
                heap.append(post)
        heapq.heapify(heap)
        while heap and len(recentTweets) < 10:
            time, tweet = heapq.heappop(heap)
            recentTweets.append(tweet)
        
        return recentTweets

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followers[followerId]:
            self.followers[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)