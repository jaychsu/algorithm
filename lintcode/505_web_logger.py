class WebLogger:
    def __init__(self):
        dummy = []
        dummy[:] = [dummy, dummy, -1]
        self.dummy = dummy
        self.size = 0

    """
    @param: timestamp: An integer
    @return: nothing
    """
    def hit(self, timestamp):
        tail = self.dummy[0]

        tail[1] = self.dummy[0] = _n = [None, None, timestamp]
        _n[0] = tail
        _n[1] = self.dummy

        self.size += 1

    """
    @param: timestamp: An integer
    @return: An integer
    """
    def get_hit_count_in_last_5_minutes(self, timestamp):
        head = self.dummy[1]

        while (head is not self.dummy and
               head[2] + 300 <= timestamp):
            _, nxt, _ = head
            self.dummy[1] = nxt
            nxt[0] = self.dummy
            head[0] = head[1] = None

            head = nxt
            self.size -= 1

        return self.size
