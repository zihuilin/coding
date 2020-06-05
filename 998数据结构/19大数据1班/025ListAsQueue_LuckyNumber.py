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

    def peek(self):
        if self.head == -1:
            return None
        else:
            return self.list[self.head]
    
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

    def print_all(self): # (1)-(2)-(3)-...
        if self.head == -1:  #空队列
            return
        elif self.tail < self.head: #tail在head前面
            for i in range(self.head, self.capacity):
                print("(" + str(self.list[i]) + ")-", end='')
            for i in range(0, self.tail+1):
                print("(" + str(self.list[i]) + ")", end='')
            if i != self.tail:
                print("-", end='')
        else: #普通情况
            for i in range(self.head, self.tail+1):
                print("(" + str(self.list[i]) + ")", end='')
            if i != self.tail:
                print("-", end='')
        print() #回车

queue = LQueue(4)
queue.put(1)
queue.put(2)
queue.put(3)
#queue.print_all()
queue.put(4)
#queue.print_all()
print(queue.get())  #1
print(queue.get())  #2
queue.put(5)
queue.print_all()
'''
n = int(input())
lucky_nums = []
max_num = 0
for i in range(n):
    num = int(input())
    if num > max_num:
        max_num = num
    lucky_nums.append(num)

index_nums = []  #存放每个幸运数字是第几个
count = 0   # 要找的幸运数字找到第几个
ln_count = 1 # 当前找到的是第几个幸运数字

q3 = LQueue(10000)
q5 = LQueue(10000)
q7 = LQueue(10000)

q3.put(3)
q5.put(5)
q7.put(7)

lucky_num = 0
while lucky_num != max_num:
    if q3.peek() <= q5.peek() and q3.peek() <= q7.peek():
        lk = q3.get() #出队q3
    elif q5.peek() <= q3.peek() and q5.peek() <= q7.peek():
        lk = q5.get() #出队q5
    else:
        lk = q7.get() #出队q7
    #判断出队的有没有重复？
    if lk != lucky_num:
        lucky_num = lk #不一样就存到luck_num里
        #如果没有重复，就让lucky_num X3 X5 X7后，入队
        q3.put(lucky_num*3)
        q5.put(lucky_num*5)
        q7.put(lucky_num*7)

        #还要放到输出的index_nums
        if lucky_num == lucky_nums[count]:
            index_nums.append(ln_count)
            count = count + 1    #题目中数字的序号
        ln_count = ln_count + 1  #幸运数字的序号


#while循环结束后，所有要求的lucky_num的序号都在index_nums里
for i in range(len(index_nums)):
    print(index_nums[i])
'''
