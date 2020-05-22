class LStack:
    def __init__(self):
        self.list = []
        self.top = -1

    def push(self, data):
        self.list.append(data)
        self.top = self.top + 1

    def pop(self):
        if self.top == -1:
            return None
        self.top = self.top - 1
        return self.list.pop()

    #如果是空栈，返回True,否则返回False
    def is_empty(self):
        if self.top == -1:
            return True
        else:
            return False

    #只返回栈顶数据，而不出栈
    def peek(self):
        if self.top == -1: #空栈
            return None
        return self.list[self.top]

s = LStack()
s.push(1)
s.push(2)
s.push(3)
print(s.peek())   # 3
print(s.is_empty()) # False
print(s.pop()) # 3
print(s.pop()) # 2
print(s.pop()) # 1
print(s.pop()) # None

print(s.peek()) # None
print(s.is_empty()) # True

