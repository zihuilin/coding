
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def print_linked_list(linked_list):
        p = linked_list
        print("head", end='')
        while p != None:
            print("(" + str(p.data) + ")->", end='')
            p = p.next
        print("None")

head = Node(1)
head.next = Node(2)
print_linked_list(head)
