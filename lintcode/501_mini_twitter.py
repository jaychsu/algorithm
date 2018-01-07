"""
Definition of Tweet:
class Tweet:
    @classmethod
    def create(cls, user_id, tweet_text):
         # This will create a new tweet object,
         # and auto fill id
"""


class MiniTwitter:
    def __init__(self):
        self.t = 0
        self.tweets = {}
        self.friends = {}

    """
    @param: user_id: An integer
    @param: tweet_text: a string
    @return: a tweet
    """
    def postTweet(self, user_id, tweet_text):
        if user_id not in self.tweets:
            self.tweets[user_id] = []

        self.t += 1
        self.tweets[user_id].append((
            self.t,
            Tweet.create(user_id, tweet_text),
        ))
        return self.tweets[user_id][-1][1]

    """
    @param: user_id: An integer
    @return: a list of 10 new feeds recently and sort by timeline
    """
    def getNewsFeed(self, user_id):
        res = []

        if user_id in self.tweets:
            res.extend(self.tweets[user_id][-10:])

        if user_id in self.friends:
            for friend_id in self.friends[user_id]:
                if friend_id in self.tweets:
                    res.extend(self.tweets[friend_id][-10:])

        if not res:
            return []

        res.sort()
        return [tweet for _, tweet in res][-10:][::-1]

    """
    @param: user_id: An integer
    @return: a list of 10 new posts recently and sort by timeline
    """
    def getTimeline(self, user_id):
        if user_id not in self.tweets:
            return []

        return [tweet for _, tweet in self.tweets[user_id]][-10:][::-1]

    """
    @param: from_id: An integer
    @param: to_id: An integer
    @return: nothing
    """
    def follow(self, from_id, to_id):
        if from_id not in self.friends:
            self.friends[from_id] = set()

        self.friends[from_id].add(to_id)

    """
    @param: from_id: An integer
    @param: to_id: An integer
    @return: nothing
    """
    def unfollow(self, from_id, to_id):
        if from_id not in self.friends:
            return

        self.friends[from_id].discard(to_id)
