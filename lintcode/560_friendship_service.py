class FriendshipService:
    def __init__(self):
        self.followers = {}
        self.followings = {}

    def getFollowers(self, user_id):
        return self.get_followers(user_id)

    def getFollowings(self, user_id):
        return self.get_followings(user_id)

    """
    @param: user_id: An integer
    @return: all followers and sort by user_id
    """
    def get_followers(self, user_id):
        if user_id in self.followers:
            return sorted(self.followers[user_id])

        return []

    """
    @param: user_id: An integer
    @return: all followings and sort by user_id
    """
    def get_followings(self, user_id):
        if user_id in self.followings:
            return sorted(self.followings[user_id])

        return []

    """
    @param: to_id: An integer
    @param: from_id: An integer
    @return: nothing
    """
    def follow(self, to_id, from_id):
        if from_id not in self.followings:
            self.followings[from_id] = set()
        self.followings[from_id].add(to_id)

        if to_id not in self.followers:
            self.followers[to_id] = set()
        self.followers[to_id].add(from_id)

    """
    @param: to_id: An integer
    @param: from_id: An integer
    @return: nothing
    """
    def unfollow(self, to_id, from_id):
        if from_id in self.followings:
            self.followings[from_id].discard(to_id)

        if to_id in self.followers:
            self.followers[to_id].discard(from_id)
