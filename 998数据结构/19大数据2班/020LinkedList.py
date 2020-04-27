class LinkedList:
    class Node:
        def __init__(self, data):
            self.data = data #数据
            self.next = None #next链接指向None

    def __init__(self):
        self.head = None  #头部一开始指向None(为空）

    def add_to_head(self, new_data):
        new_node = self.Node(new_data) #创建一个节点
        new_node.next = self.head #让新节点的next引用原来的head
        self.head = new_node #变更head为这个新节点

    def add_to_tail(self, new_data):
        #创建一个节点，存放new_data，并把这个节点插入到末尾

    def print_all(self):
        p = self.head
        while p != None:
            print(p.data)
            p = p.next

llist = LinkedList()
llist.add_to_head(4)
llist.add_to_head(2)
llist.add_to_head(1)
llist.print_all()
'''
a = Node(1)  #创建一个名为a的Node节点
b = Node(2)
c = Node(4)
a.next = b
b.next = c

print_linked_list(a)

print(a.data)
print(b.data)
print(c.data)
print(a.next.data)      #打印的b的data
print(a.next.next.data)  #打印的c的data
'''
