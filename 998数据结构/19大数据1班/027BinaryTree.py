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

class LLStack:
    def __init__(self):
        #初始化一个链表，作为栈的存储结构
        self.llist = LinkedList()

    def push(self, data):
        self.llist.add_from_tail(data)

    def pop(self):
        return self.llist.delete_from_tail()

    def peek(self):
        if self.llist.is_empty():
            return None
        else:
            return self.llist.tail.data

    def is_empty(self):
        return self.llist.is_empty()


class BinaryTree:
    class Node:
        def __init__(self, data):
            self.data = data
            self.left = None  # 一开始没有左孩子
            self.right = None # 一开始没有右孩子
    def __init__(self):
        self.root = None

    def dfs(self, node):
        if node != None:   #判断递归出口
            self.dfs(node.left)  #访问左子树  （左）
            print(node.data)        #访问这个节点（中）
            self.dfs(node.right) #访问右子树  （右）

    def dfs_non_recursive(self):
        stack = LLStack() # 用于辅助的栈
        node = self.root
        while node is not None:
            while node is not None: #入栈右孩子，节点本身
                if node.right is not None:
                    stack.push(node.right) #入栈右孩子
                stack.push(node) #入栈该节点
                node = node.left #走到左孩子，继续循环
            #此时，刚刚入栈的是最小（最左的）节点
            node = stack.pop() #此时出栈的是最小的节点
            while node.right is None and stack.is_empty() is not True:
                print(node.data) #访问该节点
                node = stack.pop() #访问那些单独一溜的节点
            print(node.data) #先访问这个节点
            if stack.is_empty():
                break
            else: #非空，也就是有右子树
                node = stack.pop() # 弹出右子树的根节点


    def bfs(self):
        queue = LLQueue() #辅助队列
        if self.root == None:   #根为空，空树
            return
        queue.put(self.root)
        #使用一个while循环，广度优先遍历二叉树
        while queue.is_empty() != True:
            node = queue.get() #出队首
            print(node.data)
            if node.left != None:  #入队左孩子
                queue.put(node.left)
            if node.right != None:  #入队右孩子
                queue.put(node.right)


    def __find_min(self, node):
        '''  非递归版本
        #找到最左边的节点，返回它的data
        while node.left is not None: #如有左孩子
            node = node.left #走向左孩子
        return node.data
        '''
        if node.left is None: #这个节点没有左子树
            return node.data
        else:
            return self.__find_min(node.left)

    def find_min(self):
        if self.root is None:
            return None
        else:
            return self.__find_min(self.root)

tree = BinaryTree() #声明一个二叉树
tree.root = BinaryTree.Node(5)
tree.root.left = BinaryTree.Node(3)
tree.root.right = BinaryTree.Node(7)
tree.root.left.left = BinaryTree.Node(1)
tree.root.left.left.right = BinaryTree.Node(2)
tree.root.left.right = BinaryTree.Node(4)
tree.root.right.left = BinaryTree.Node(6)
tree.root.right.right = BinaryTree.Node(8)

print(tree.find_min())
#tree.dfs(tree.root) #从根节点开始遍历
#tree.dfs_non_recursive() #从根节点开始遍历
#tree.bfs() #广度优先遍历
