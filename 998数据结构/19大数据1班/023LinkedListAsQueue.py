class LinkedList:
    def __init__(self): #构造一个空链表
        self.head = None
        self.tail = None

    class Node:
        def __init__(self):
            self.data = None
            self.next = None

        def __init__(self, d):
            self.data = d
            self.next = None

    def is_empty(self):
        if self.head == None:
            return True
        else:
            return False

    def add_from_tail(self, d):
        new_node = self.Node(d)
        if self.head == None: #空链表
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def add_from_head(self, d):
        new_node = self.Node(d)
        if self.head == None: #空链表
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def print_all(self):
        node = self.head
        while node != None:
            print("(" + str(node.data) + ")->", end='')
            node = node.next
        print("None")

    def is_in_list(self, d):
        node = self.head
        while node != None :
            if node.data == d:
                return True
            node = node.next
        return False

    def delete_from_head(self):
        if self.head == None: #空链表
            return None       #没得head可删
        elif self.head == self.tail: #只有一个节点
            data = self.head.data
            self.head = None
            self.tail = None
            return data  #返回被删数据
        else:
            data = self.head.data
            self.head = self.head.next
            return data
    
    def delete_from_tail(self):
        data = None
        if self.head == None: #空链表
            return data
        elif self.head == self.tail: #只有一个节点
            data = self.tail.data
            self.head = None
            self.tail = None
        else:
            data = self.tail.data
            p = self.head
            while p.next != self.tail: #如果p后面不是tail
                p = p.next #让p向后移动
            self.tail = p #tail引用原来倒数第2个节点
            self.tail.next = None
        return data

    def delete_node(self, data):
        #1. 空链表
        if self.head == None:
            return None
        dtd = None #存放被删除数据
        #只有一个节点且是被删节点
        if self.head == self.tail and self.head.data == data:
            dtd = data
            self.head = None
            self.tail = None
        elif self.head.data == data : #要删除的节点是head
            dtd = data
            self.head = self.head.next
        else: #普通情况：
            pre_node = self.head
            node = pre_node.next
            while node != None and node.data != data:
                pre_node = pre_node.next
                node = pre_node.next
            if node != None:
                dtd = data
                pre_node.next = node.next
                if node == self.tail: #要删除的节点是tail
                    self.tail = pre_node
            else:
                return None
        return dtd

class LLQueue:
    def __init__(self):
        #初始化用于存储数据的LinkedList
        self.list = LinkedList()

    def put(self, data):
        self.list.add_from_tail(data)

    def get(self):
        return self.list.delete_from_head()

    def peek(self):
        if self.list.is_empty():
            return None
        else:
            return self.list.head.data

    def is_empty(self):
        return self.list.is_empty()

queue = LLQueue()
queue.put(1)
queue.put(2)
queue.put(3)
print(queue.get())  # 1
print(queue.get())  # 2
print(queue.get())  # 3
print(queue.get())  # None
print(queue.is_empty())  # True
