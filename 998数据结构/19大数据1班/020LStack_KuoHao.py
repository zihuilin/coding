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

string = input()

#遍历string的各个字符
    #若字符为'(' :入栈
    #另外，若字符为'）' :出栈
        #如果没得出栈：no
#遍历结束后，判断栈非空： no
#否则： yes

