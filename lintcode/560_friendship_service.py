class FriendshipService:

    followers = {}
    followings = {}

    """
    @param: user_id: An integer
    @return: all followers and sort by user_id
    """
    def get_followers(self, user_id):
        return self.getFollowers(user_id)

    def getFollowers(self, user_id):
        if user_id in self.followers:
            return sorted(self.followers[user_id])

        return []

    """
    @param: user_id: An integer
    @return: all followings and sort by user_id
    """
    def get_followings(self, user_id):
        return self.getFollowings(user_id)

    def getFollowings(self, user_id):
        if user_id in self.followings:
            return sorted(self.followings[user_id])

        return []

    """
    @param: to_user_id: An integer
    @param: from_user_id: An integer
    @return: nothing
    """
    def follow(self, to_user_id, from_user_id):
        if to_user_id not in self.followers:
            self.followers[to_user_id] = set()
        if from_user_id not in self.followings:
            self.followings[from_user_id] = set()

        self.followers[to_user_id].add(from_user_id)
        self.followings[from_user_id].add(to_user_id)

    """
    @param: to_user_id: An integer
    @param: from_user_id: An integer
    @return: nothing
    """
    def unfollow(self, to_user_id, from_user_id):
        if to_user_id in self.followers:
            self.followers[to_user_id].discard(from_user_id)
        if from_user_id in self.followings:
            self.followings[from_user_id].discard(to_user_id)
