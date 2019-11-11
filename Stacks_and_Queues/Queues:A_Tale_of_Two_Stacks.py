class MyQueue(object):
    def __init__(self):
        self.mouth = []
        self.butt = []

    def peek(self):
        self.digest()
        return self.butt[-1]

    def pop(self):
        self.digest()
        return self.butt.pop()

    def put(self, value):
        self.mouth.append(value)

    def digest(self):
        if not self.butt:
            while self.mouth:
                self.butt.append(self.mouth.pop())








