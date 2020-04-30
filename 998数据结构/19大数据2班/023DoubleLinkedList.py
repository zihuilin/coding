class DoubleLinkedList:
    class Node:
        def __init__(self, data):
            self.data = data #数据
            self.prev = None #prev链接指向None
            self.next = None #next链接指向None

    def __init__(self):
        self.head = None  #头部一开始指向None(为空）
        self.tail = None  #尾部一开始指向None(为空）

    def add_to_head(self, new_data):
        #0 创建一个新的Node
        new_node = self.Node(new_data)
        #1 若链表为空： head和tail都是这个新节点
        if self.head == None :
            self.head = new_node
            self.tail = new_node
        #2 若链表非空：
        else:
            #2.1 让新节点的next为原来的head
            new_node.next = self.head
            #2.2 让原head的prev指向新节点
            self.head.prev = new_node
            #2.3 让head引用新节点
            self.head = new_node

    def delelte_from_head(self):
        data = None  #要返回的数据
        #1 链表为空： 返回None
        if self.head == None:
            data = None
        #2 链表只有1个节点：
        if self.head == self.tail:
            #2.1 记下这个节点的数据
            data = self.head.data
            #2.2 让head和tail都为空
            self.head = None
            self.tail = None
        #3 链表不只有1个节点：
        else:
            #3.1 记录原head的data
            data = self.head.data
            #3.2 让head引用原head的next
            self.head = self.head.next
            #3.3 让新head的prev为None
            self.head.prev = None
        return data

    def add_to_tail(self,new_data):
        new_node = self.Node(new_data)
        if self.head == None: #空链表
            self.head == new_node
            self.tail == new_node
        else:
            new_node.prev = self.tail
            self.tail = new_node
            self.tail.prev.next = self.tail

    def print_all(self):
        print("head->", end='')
        p = self.head
        while p != None:
            print("(" + str(p.data) + ")->", end='')
            p = p.next
        print("None")

dll = DoubleLinkedList()
dll.add_to_head(1)
dll.print_all()
dll.add_to_head(2)
dll.print_all()
dll.delelte_from_head()
dll.print_all()
