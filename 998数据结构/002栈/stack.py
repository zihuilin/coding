class LStack():
    def __init__(self):
        self._top = -1
        self._elems = []

    def is_empty(self):
        return self._top == -1 

    def top(self):
        if self.is_empty():
            raise StackUnderflow("in LStack.top()")
        return self._elems[self._top]

    def push(self, elem):
        self._elems.append(elem)
        self._top = self._top + 1

    def pop(self):
       if self.is_empty():
           raise StackUnderflow("in LStack.pop()")
       self._top = self._top - 1
       return self._elems[self._top + 1] 

stack = LStack()
stack.push(3)
stack.push(5)
print(stack.top())

while not stack.is_empty():
    print(stack.pop())
