class Vector2D(object):
    # @param G {List[List[int]]}
    def __init__(self, G):
        self.x = self.y = 0
        self.G = G

    # @return {int} a next element
    def next(self):
        if not self.hasNext():
            return

        res = self.G[self.x][self.y]
        self.y += 1
        return res

    # @return {boolean} true if it has next element
    # or false
    def hasNext(self):
        # if `y` get to end or new `x` is empty
        while (self.x < len(self.G) and
               self.y >= len(self.G[self.x])):
            self.x += 1
            self.y = 0

        return self.x < len(self.G)

# Your Vector2D object will be instantiated and called as such:
# i, v = Vector2D(vec2d), []
# while i.hasNext(): v.append(i.next())
