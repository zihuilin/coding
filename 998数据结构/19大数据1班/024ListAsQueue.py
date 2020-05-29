class LQueue:
    def __init__(self, capacity):
        self.list = [0] * capacity # 一次初始化
        self.capacity = capacity
        #刚初始化好的队列为空
        self.head = None
        self.tail = None 

    def is_empty(self):
        if self.head == None:
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

