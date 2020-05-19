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

    def add_from_tail(self. d):
        #完成从尾部插入数据

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

linkedList = LinkedList() #构造一个空链表
linkedList.add_from_head(33)
linkedList.print_all()
linkedList.add_from_head(22)
linkedList.print_all()
linkedList.add_from_head(11)
linkedList.print_all()

