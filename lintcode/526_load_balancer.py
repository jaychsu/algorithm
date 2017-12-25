from random import randint


class LoadBalancer:
    def __init__(self):
        self.ids = []
        self.id2index = {}

    """
    @param: svrid: add a new server to the cluster
    @return: nothing
    """
    def add(self, svrid):
        if svrid in self.id2index:
            return

        self.ids.append(svrid)
        self.id2index[svrid] = len(self.ids) - 1

    """
    @param: svrid: svrid remove a bad server from the cluster
    @return: nothing
    """
    def remove(self, svrid):
        if svrid not in self.id2index:
            return

        i = self.id2index[svrid]
        _svrid = self.ids[-1]
        self.ids[i], self.ids[-1] = self.ids[-1], self.ids[i]
        self.ids.pop()

        self.id2index[_svrid] = i
        del self.id2index[svrid]

    """
    @return: pick a server in the cluster randomly with equal probability
    """
    def pick(self):
        i = randint(0, len(self.ids) - 1)
        return self.ids[i]
