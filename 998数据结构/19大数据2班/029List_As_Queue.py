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

    def print_all(self): #打印队列 (4)-(2)-(15)...(6)
        print(self.list)
        return None

q = LQueue(6)
q.put(4)
q.put(2)
q.put(5)
q.print_all()  #(4)-(2)-(5)

