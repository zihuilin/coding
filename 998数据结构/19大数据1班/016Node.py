class Node:
    def __init__(self):
        self.data = None
        self.next = None

    def __init__(self, d):
        self.data = d
        self.next = None

def print_all(node):
    while node != None:
        print("(" + str(node.data) + ")->", end='')
        node = node.next
    print("None")

node1 = Node(11)
node2 = Node(22)
node1.next = node2 #让node1链接到node2
node3 = Node(33)
node2.next = node3
print(node1.data)
print(node2.data)
print(node1.next.data) #等同于print(node2.data)
print(node2.next.data) #等同于print(node3.data)
print(node1.next.next.data) #等同于print(node3.data)
print_all(node1)   # (11)->(22)->(33)->None
