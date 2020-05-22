class LQueue:
    def __init__(self, size): #size为最大的存储大小
        self.list = [0] * size; #一次性初始存储空间
        self.size = size
        self.head = -1
        self.tail = -1

    def is_empty(self):
        if self.head == -1:
            return True
        else:
            return False

    def is_full(self):
        if (self.head == 0 and self.tail == self.size -1) or self.head == self.tail + 1:
            return True
        else:
            return False

    def put(self, data): #入队
        if self.is_full():
            print("Queue is full.")
        elif self.tail == self.size -1:
            self.tail = 0
            self.list[self.tail] = data
        elif self.tail == -1:
            self.tail = 0
            self.head = 0
            self.list[self.tail] = data
        else:
            self.tail = self.tail + 1
            self.list[self.tail] = data

    def get(self):
        #1. 空队列
        if self.head == -1:
            return None
        data = self.list[self.head]
        #2. 只有一个数据: head,tail都为-1
        if self.head == self.tail:
            self.head = -1
            self.tail = -1
        #3. 普通情况: head向后移
        elif self.head != self.size - 1:
            self.head = self.head + 1
        #4. 特别情况：head移动到开头
        else:
            self.head = 0
        return data

    def print_all(self): #打印队列 (4)-(2)-(15)...(6)
        if self.head == -1: #空队列
            print("空队列")
            return
        elif self.head <= self.tail: #head在tail前面
            for i in range(self.head, self.tail+1):
                print("(" + str(self.list[i]) + ")", end='')
                if i!= self.tail:
                    print("-", end='')
        elif self.head > self.tail: #head在tail后面
            for i in range(self.head, self.size):
                print("(" + str(self.list[i]) + ")-", end='')
            for i in range(0, self.tail+1):
                print("(" + str(self.list[i]) + ")", end='')
                if i!= self.tail:
                    print("-", end='')
        print()



q = LQueue(6)
q.put(1)
q.put(2)
q.print_all() # (1)-(2)
print(q.get()) # 1
q.print_all()  # (2)
print(q.get()) # 2
q.print_all()  # 空队列 
print(q.get()) # 2
q.put(1)
q.put(2)
q.put(3)
q.put(4)
q.put(5)
q.put(6)
print(q.get()) # 2
q.put(7)
q.print_all()  # 空队列 
print(q.list)
print(q.get()) # 2
q.print_all()  # 空队列 
print(q.list)

