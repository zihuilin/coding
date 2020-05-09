class LStack:
    def __init__(self):
        self.list = []
        self.top = -1  #整数表示栈顶的位置

    #入栈
    def push(self, data):
        self.list.append(data)
        self.top = self.top + 1

    #出栈
    def pop(self):
        if self.top >= 0: #栈非空
            self.top = self.top - 1
            return self.list.pop()
        else:
            return None #空栈没得pop

    #判断栈是否为空，空就返回true
    def is_empty(self):
        if self.top < 0:
            return True
        else:
            return False

stack = LStack()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.is_empty())  # False
print(stack.pop())  # 3
print(stack.pop())  # 2
print(stack.pop())  # 1
print(stack.pop())  # 栈空：pop出None
print(stack.is_empty())  # True

