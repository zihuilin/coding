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

dengshi = str(input())
stack = LStack()
flag = True

for i in range(len(dengshi)):
    if dengshi[i] == '(':
        stack.push('(')
    elif dengshi[i] == ')':
        if stack.pop() == None: #判断栈为空
            flag = False
            break;

if flag == True and stack.is_empty():
    flag = True
else:
    flag = False

if flag:
    print("yes")
else:
    print("no")





