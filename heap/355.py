class Twitter:

    def __init__(self):
        self.users = defaultdict(set)
        self.posts = defaultdict(list)
        self.time = 0
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.posts[userId].append((self.time, tweetId))
        self.time -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        
        result = []
        max_heap = []
        # each user also follows themselves since we want their posts as well

        self.users[userId].add(userId)

        followers = self.users[userId]

        for each in followers:
            # if this particular user actually does have posts
            if each in self.posts:
                index = len(self.posts[each]) - 1
                time, tweet = self.posts[each][index]
                heapq.heappush(max_heap, (time, tweet, each, index - 1))
        
        # heapq.heapify(max_heap)
        while len(result) < 10 and max_heap:
            # print(max_heap[0])
            time, tweet, followeeId, index = heapq.heappop(max_heap)
            result.append(tweet)
            if index >= 0:
                time, tweet = self.posts[followeeId][index]
                heapq.heappush(max_heap, (time, tweet, followeeId, index - 1))

        return result


        

    def follow(self, followerId: int, followeeId: int) -> None:

        if followerId != followeeId:
            self.users[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.users[followerId]:
            self.users[followerId].remove(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)