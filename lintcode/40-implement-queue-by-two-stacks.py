class MyQueue:
    def __init__(self, ):
        self.stack1 = []
        self.stack2 = []

    """
    @param: element: An integer
    @return: nothing
    """
    def push(self, element):
        self.stack1.append(element)

    """
    @return: An integer
    """
    def pop(self, ):
        self.top()
        return self.stack2.pop()

    """
    @return: An integer
    """
    def top(self, ):
        # While `self.stack2` is empty, get element from `self.stack1`
        # step0/ stack1: [1, 2, 3], stack2: []
        # step1/ stack1: [], stack2: [3, 2, 1]
        # step2/ stack1: [4, 5, 6], stack2: [3, 2] // 1
        # step3/ stack1: [4, 5, 6], stack2: [] // 2, 3
        # step4/ stack1: [7, 8], stack2: [6, 5, 4]
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2[-1]
