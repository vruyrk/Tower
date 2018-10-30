class Stack:
    def __init__(self):
        self.stack = []

    def pop(self):
        if self.is_empty():
            return None
        else:
            return self.stack.pop()

    def push(self, val):
        return self.stack.append(val)

    def peak(self):
        if self.is_empty():
            return None
        else:
            return self.stack[-1]

    def size(self):
        return len(self.stack)

    def is_empty(self):
        return self.size() == 0

class Tower():
    def __init__(self):
        self.first = Stack()
        self.mytemp = Stack()
        self.last = Stack()

    def ascending(self):
        while self.first.is_empty() == False:
            if self.last.is_empty():
                self.last.push(self.first.pop())
            else:
                mytemp = self.first.pop()
                if mytemp >= self.last.peak():
                    self.last.push(mytemp)
                else:
                    while mytemp < self.last.peak():
                        self.mytemp.push(self.last.pop())
                    self.last.push(mytemp)
                    while self.mytemp.is_empty() == False:
                        self.last.push(self.mytemp.pop())
            print(self.last.stack)

def main():
    list = Tower()
    list.first.stack = [2, 4, 1]
    list.ascending()

main()