"""
Definition of Tweet:
class Tweet:
    @classmethod
    def create(cls, user_id, tweet_text):
         # This will create a new tweet object,
         # and auto fill id
"""

from collections import OrderedDict


class MiniTwitter:
    timestamp = 0
    tweets = {}
    friends = {}

    """
    @param: user_id: An integer
    @param: tweet_text: a string
    @return: a tweet
    """
    def postTweet(self, user_id, tweet_text):
        if user_id not in self.tweets:
            self.tweets[user_id] = OrderedDict()

        self.timestamp += 1
        self.tweets[user_id][self.timestamp] = Tweet.create(user_id, tweet_text)

        return self.tweets[user_id][self.timestamp]

    """
    @param: user_id: An integer
    @return: a list of 10 new feeds recently and sort by timeline
    """
    def getNewsFeed(self, user_id):
        result = []

        if user_id in self.tweets:
            result += [
                item
                for item in self.tweets[user_id].items()[-10:]
            ]

        if user_id in self.friends:
            for friend_id in self.friends[user_id]:
                if friend_id in self.tweets:
                    result += [
                        item
                        for item in self.tweets[friend_id].items()[-10:]
                    ]

        if not result:
            return []

        result.sort(key=lambda item: item[0])
        return [
            tweet
            for timestamp, tweet in result[-10:]
        ][::-1]

    """
    @param: user_id: An integer
    @return: a list of 10 new posts recently and sort by timeline
    """
    def getTimeline(self, user_id):
        if user_id not in self.tweets:
            return []

        return [
            tweet
            for tweet in self.tweets[user_id].values()[-10:]
        ][::-1]

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
        if (from_user_id not in self.friends or
            to_user_id not in self.friends[from_user_id]):
            return

        self.friends[from_user_id].remove(to_user_id)
