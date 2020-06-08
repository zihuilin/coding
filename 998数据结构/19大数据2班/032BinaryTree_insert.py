class LinkedList:
    class Node:
        def __init__(self, data):
            self.data = data #数据
            self.next = None #next链接指向None

    def __init__(self):
        self.head = None  #头部一开始指向None(为空）
        self.tail = None  #尾部一开始指向None(为空）

    def is_empty(self):
        if self.head == None:
            return True
        else:
            return False

    def add_to_head(self, new_data):
        new_node = self.Node(new_data) #创建一个节点
        if self.head == None:
            self.tail = new_node
        new_node.next = self.head #让新节点的next引用原来的head
        self.head = new_node #变更head为这个新节点

    def delete_from_head(self):
        #1. 当LinkedList为空时
        if self.head == None:
            return None # None表示没有可以删除的节点
        if self.head == self.tail :
            d = self.head.data  #记录原来头部的数据
            #让head和tail都引用None
            self.head = None
            self.tail = None
        #3. 当多于1个节点的时候：
        else:
            d = self.head.data  #记录原来头部的数据
            #让head引用原来head的next节点
            self.head = self.head.next
        return d
        #还要返回被删除节点中的数据

    def delete_from_tail(self):
        d = None #用来返回被删除的数据
        if self.head == None: #1. 空链表
            d = None
        elif self.head == self.tail: #2. 只有1个节点：
            d = self.tail.data
            self.head = None
            self.tail = None
        else: #3. 使用while循环找tail前面的节点
            d = self.tail.data
            p = self.head
            while p.next != self.tail: #如果p后面不是tail
                p = p.next  #p向后移动
            self.tail = p #更改tail为tail前面的节点
            self.tail.next = None #末尾的next总是None
        return d

    def delete_node(self, data_to_be_deleted):
        d = data_to_be_deleted
        if self.head == None:  #空链表
            return None
        elif self.head == self.tail and self.head.data == d :
            #只有一个节点，这个节点是要删除的节点
            self.head = None
            self.tail = None
            return d
        else:
            if self.head.data == d:
                self.head = self.head.next
                return d
            else: #通过while循环，寻找d前面的节点
                p = self.head
                while p.next != None and p.next.data != d:
                    p = p.next # 向后移动
                if p.next != None:
                    p.next = p.next.next
                    return d
        #没找到。。。
        return None # None表示没有找到要删除的节点


    #创建一个节点，存放new_data，并把这个节点插入到末尾
    def add_to_tail(self, new_data):
        new_node = self.Node(new_data)
        if self.head == None: #空链表
            self.head = new_node
        else: #不是空链表
            self.tail.next = new_node
        self.tail = new_node


    def print_all(self):
        print("head->", end='')
        p = self.head
        while p != None:
            print("(" + str(p.data) + ")->", end='')
            p = p.next
        print("None")

class Queue:
    def __init__(self):
        self.llist = LinkedList()

    def put(self, data): #入队
        self.llist.add_to_tail(data)

    def get(self):    #出队
        return self.llist.delete_from_head()

    def peak(self):   #只看队首，但不出队
        if self.is_empty():
            return None   #空队列
        else:
            return self.llist.head.data

    def is_empty(self): #是否为空队列
        return self.llist.is_empty()

class LinkedListStack:
    def __init__(self):
        self.llist = LinkedList()

    def push(self, data):  #入栈
        self.llist.add_to_tail(data)

    def pop(self):  #堂上练习
        return self.llist.delete_from_tail()

    def peak(self):
        return self.llist.get_tail()

    def is_empty(self):
        return self.llist.is_empty()

class BinaryTree:
    class Node:
        def __init__(self, d):
            self.data = d;
            self.left = None    #左后继
            self.right = None   #右后继

    def __init__(self):
        self.root = None

    def dfs(self, n):
        if n != None:
            self.dfs(n.left) #再看左后继
            print(n.data)  #(1)先看此节点
            self.dfs(n.right) #再看右后继

    def inorder_dfs_non_recursive(self):
        s = LinkedListStack()
        node = self.root
        while node != None:
            while node != None:
                if node.right != None:
                    s.push(node.right)#入栈右后继
                s.push(node)          #入栈中间节点
                node = node.left      #不断向左
            node = s.pop()   #出栈一个（最左边的节点）
            while s.is_empty() != True and node.right == None:
                print(node.data)  #访问这个节点
                node = s.pop()    #继续出栈左边孤单节点
            #此时，要么s为空，要么node有右后继
            print(node.data) #访问这个节点
            if s.is_empty() != True:
                node = s.pop()   #得到右边节点，访问右子树
            else:
                node = None  #栈空，意味着遍历结束


    def bfs(self):
        q = Queue() #用于辅助的队列
        #如果根节点不为空
        if self.root != None:
            #入队根节点
            q.put(self.root)
        #while 队列非空
        while q.is_empty() != True:
            #出队一个，打印节点的数据
            node = q.get()
            print(node.data)
            #入队这个节点的左右后继
            if node.left != None:
                q.put(node.left)
            if node.right != None:
                q.put(node.right)
    def insert(self, data):
        new_node = BinaryTree.Node(data)
        if self.root == None: # 空树
            self.root = new_node #要插入的就是根节点
        else: # 不是空树
        #从根开始，搜索一个合适的位置，放新节点
            p = self.root #p_node为合适位置的父节点
            #在一个循环里，通过比较大小，向下移动
            while True: #如果能向下，就向下走
                if data < p.data:
                    if p.left == None:
                        p.left = new_node #挂在左边
                        break #不需要再向下走了
                    else:
                        p = p.left #有左孩子，向左走
                elif data > p.data:
                    if p.right == None:
                        p.right = new_node #挂在右边
                        break #不需要再向下走了
                    else:
                        p = p.right #有右孩子，向右走
                else: #相同，也就是树上已经有了这个数据
                    break

    def find_min(self):
        if self.root is None: #根为空：空树
            return None
        else:
            return self.__find_min(self.root) #从根节点开始寻找最小的节点
    
    def __find_min(self, node):
        ''' 非递归的实现，用while循环
        while node.left is not None:  # 有左孩子
            node = node.left          # 走到左孩子这个节点
        #while结束时，该节点是没有左孩子
        return node.data #返回该结点上的数据（data）
        '''
        #递归的思路：
        if node.left is None: # 如果该节点没有左子树
            return node.data  # 出口：返回这个节点的数据
        else: #否则，在有左子树的情况下
            return self.__find_min(node.left)#返回 它左子树上最小的节点的数据（递归调用）

tree = BinaryTree()
tree.insert(5)
tree.insert(3)
tree.insert(8)
#tree.dfs(tree.root)
print(tree.root.left.data) # 3
print(tree.root.right.data) # 8
tree.insert(1)
print(tree.root.left.left.data) # 1
'''
tree.root = BinaryTree.Node(5)
tree.root.left = BinaryTree.Node(3)
tree.root.left.left = BinaryTree.Node(1)
tree.root.left.right = BinaryTree.Node(4)
tree.root.right = BinaryTree.Node(8)
tree.root.right.left = BinaryTree.Node(7)
tree.root.right.right = BinaryTree.Node(10)
tree.root.right.right.left = BinaryTree.Node(9)
tree.root.right.right.right = BinaryTree.Node(11)
'''

#print(tree.find_min())  # 1
#tree.bfs()
#tree.inorder_dfs_non_recursive()
