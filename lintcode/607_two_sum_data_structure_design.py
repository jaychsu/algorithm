class TwoSum:
    count = {}

    """
    @param: number: An integer
    @return: nothing
    """
    def add(self, number):
        if number in self.count:
            self.count[number] += 1
        else:
            self.count[number] = 1

    """
    @param: value: An integer
    @return: Find if there exists any pair of numbers which sum is equal to the value.
    """
    def find(self, value):
        for num in self.count:
            remaining = value - num
            if remaining not in self.count:
                continue
            if remaining != num:
                return True
            if remaining == num and self.count[num] > 1:
                return True
        return False
