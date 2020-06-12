class AVLTree:
    class Node:
        def __init__ (self, data):
            self.data = data
            self.height = 0
            self.left = self.right = None

    def __init__(self):
        self.root = None

    def height(self, node):
        if node is None:
            return -1
        else:
            return node.height
    def __updateHeight(self, node):
        if node is None:
            return
        node.height = max(self.height(node.left), self.height(node.right)) + 1

    def printNode(self, node):
        if node is self.root:
            print("R(%d,%d) " % (node.data, node.height), end='')
        else:
            print("(%d,%d) " % (node.data, node.height), end='')

    def dfs(self):
        self.__dfs(self.root)
        print()

    def __dfs(self, node):
        if node is None:
            return
        else:
            self.__dfs(node.left)
            self.printNode(node)
            self.__dfs(node.right)

    def add(self, data):
        self.root = self.__add(data, self.root)

    def __add(self, data, node):
        if node is None:
            return self.Node(data)
        elif data < node.data:
            node.left = self.__add(data, node.left)
            if self.height(node.left) - self.height(node.right) > 1:
                if data < node.left.data:
                    node = self.__rotateLeft(node)
                else:
                    node =self.__doubleRotateLeft(node)
        elif data > node.data:
            node.right = self.__add(data, node.right)
            if self.height(node.right) - self.height(node.left) > 1:
                if data > node.right.data:
                    node = self.__rotateRight(node)
                else:
                    node = self.__doubleRotateRight(node)
        #else: Duplicate data, do nothing

        self.__updateHeight(node)
        return node

    def __rotateLeft(self, node):
        leftNode = node.left
        node.left = leftNode.right
        leftNode.right = node
        self.__updateHeight(node)
        self.__updateHeight(leftNode)
        return leftNode

    def __rotateRight(self, node):
        rightNode = node.right
        node.right = rightNode.left
        rightNode.left = node
        self.__updateHeight(node)
        self.__updateHeight(rightNode)
        return rightNode

    def __doubleRotateLeft(self, node):
        node.left = self.__rotateRight(node.left)
        return self.__rotateLeft(node)

    def __doubleRotateRight(self, node):
        node.right = self.__rotateLeft(node.right)
        return self.__rotateRight(node)

    def find_min(self):
        return self.__find_min(self.root).data

    def __find_min(self, node):
        if node is None:
            return None
        elif node.left is None:
            return node
        else:
            return self.__find_min(node.left)

    def find_max(self):
        return self.__find_max(self.root).data

    def __find_max(self, node):
        if node is None:
            return Node
        elif node.right is None:
            return node
        else:
            return self.__find_max(node.right)

    def remove(self, data):
        self.root = self.__remove(data, self.root)

    def __remove(self, data, node):
        if node is None:
            return None
        elif data < node.data:
            node.left = self.__remove(data, node.left)
        elif data > node.data:
            node.right = self.__remove(data, node.right)
        elif node.left is not None and node.right is not None:
            node.data = self.__find_min(node.right).data
            node.right = self.__remove(node.data, node.right)
        elif node.left is not None:
            node = node.left
        else:
            node = node.right
        self.__updateHeight(node)
        return node

t = AVLTree()
t.add(3)
t.add(2)
t.add(1)
t.dfs()
t.add(4)
t.add(5)
t.dfs()
t.add(6)
t.dfs()
t.add(7)
t.dfs()
t.add(16)
t.add(15)
t.dfs()
t.add(14)
t.dfs()
t.add(13)
t.dfs()
t.add(12)
t.dfs()
print(t.find_min())
t.remove(7)
print("dfs")
t.dfs()


