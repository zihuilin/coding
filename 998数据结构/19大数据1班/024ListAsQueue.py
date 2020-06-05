class LQueue:
    def __init__(self, capacity):
        self.list = [0] * capacity # 一次初始化
        self.capacity = capacity
        #刚初始化好的队列为空
        self.head = -1
        self.tail = -1

    def is_empty(self):
        if self.head == -1:
            return True
        else:
            return False
    
    def is_full(self):
        if (self.head == 0 and self.tail == self.capacity - 1) or (self.tail == self.head - 1):
            return True
        else:
            return False
    
    def put(self, data):
        #1 队列已满
        if self.is_full():
            print("Queue is full")
            return;
        #2 队列为空
        elif self.is_empty():
            self.head = 0
            self.tail = 0
        #3 tail在最后的位置上
        elif self.tail == self.capacity - 1:
            self.tail = 0
        #4 普遍的情况
        else:
            self.tail = self.tail + 1
        self.list[self.tail] = data

    def get(self):
        #1 队列为空：返回None
        if self.is_empty():
            return None
        value = self.list[self.head]
        #2 队列只有1个元素：出队后，队列为空
        if self.head == self.tail:
            self.head = -1
            self.tail = -1
        #3 head位于最后，出队后，head为0
        elif self.head == self.capacity - 1:
            self.head = 0
        #4 普通的情况：出队后，head向后移动
        else:
            self.head = self.head + 1
        return value

queue = LQueue(4)
queue.put(1)
queue.put(2)
queue.put(3)
queue.put(4)
print(queue.get())  # 1
queue.put(5)  # [5,2,3.4]
print(queue.get())  # 2
queue.put(6)  # [5,6,3.4]
queue.put(6)  # full queue

