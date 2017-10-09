'''
Definition of Tweet:
class Tweet:
    @classmethod
    def create(cls, user_id, tweet_text):
         # This will create a new tweet object,
         # and auto fill id
'''

class MiniTwitter:

    def __init__(self):
        self.timestamp = 0
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

        self.timestamp += 1
        tweet = Tweet.create(user_id, tweet_text)
        self.tweets[user_id].append((self.timestamp, tweet))
        return tweet

    """
    @param: user_id: An integer
    @return: a list of 10 new feeds recently and sort by timeline
    """
    def getNewsFeed(self, user_id):
        newsfeed = []
        if user_id in self.tweets:
            newsfeed += self.tweets[user_id][-10:]

        if user_id in self.friends:
            for friend_id in self.friends[user_id]:
                if friend_id in self.tweets:
                    newsfeed += self.tweets[friend_id][-10:]

        newsfeed.sort(key=lambda tweet: tweet[0])
        return [tweet[1] for tweet in newsfeed[-10:][::-1]]

    """
    @param: user_id: An integer
    @return: a list of 10 new posts recently and sort by timeline
    """
    def getTimeline(self, user_id):
        if user_id in self.tweets:
            return [tweet[1] for tweet in self.tweets[user_id][-10:][::-1]]
        else:
            return []

    """
    @param: from_user_id: An integer
    @param: to_user_id: An integer
    @return: nothing
    """
    def follow(self, from_user_id, to_user_id):
        if from_user_id not in self.friends:
            self.friends[from_user_id] = set()

        self.friends[from_user_id].add(to_user_id)

    """
    @param: from_user_id: An integer
    @param: to_user_id: An integer
    @return: nothing
    """
    def unfollow(self, from_user_id, to_user_id):
        if any([
            from_user_id not in self.friends,
            to_user_id not in self.friends[from_user_id],
        ]):
            return

        self.friends[from_user_id].remove(to_user_id)
