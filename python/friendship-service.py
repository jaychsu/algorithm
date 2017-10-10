class FriendshipService:

    def __init__(self):
        self.followers = {}
        self.followings = {}

    """
    @param: user_id: An integer
    @return: all followers and sort by user_id
    """
    def getFollowers(self, user_id):
        if user_id in self.followers:
            self.followers[user_id].sort()
            return [id for id in self.followers[user_id]]
        else:
            return []

    """
    @param: user_id: An integer
    @return: all followings and sort by user_id
    """
    def getFollowings(self, user_id):
        if user_id in self.followings:
            self.followings[user_id].sort()
            return [id for id in self.followings[user_id]]
        else:
            return []

    """
    @param: from_user_id: An integer
    @param: to_user_id: An integer
    @return: nothing
    """
    def follow(self, from_user_id, to_user_id):
        if from_user_id not in self.followings:
            self.followings[from_user_id] = set()
        self.followings[from_user_id].add(to_user_id)

        if to_user_id not in self.followers:
            self.followers[to_user_id] = set()
        self.followers[to_user_id].add(from_user_id)

    """
    @param: from_user_id: An integer
    @param: to_user_id: An integer
    @return: nothing
    """
    def unfollow(self, from_user_id, to_user_id):
        if all([
            from_user_id in self.followings,
            to_user_id in self.followings[from_user_id],
        ]):
            self.followings[from_user_id].remove(to_user_id)
        if all([
            to_user_id in self.followers,
            from_user_id in self.followers[to_user_id],
        ]):
            self.followers[to_user_id].remove(from_user_id)
