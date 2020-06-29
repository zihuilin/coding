class AVLTree:
    class Node:
        def __init__(self, data):
            self.data = data
            self.left = self.right = None
            self.height = 0

    def __init__(self):
        self.root = None

    def printNode(self, node):
        if node is self.root:
            print("R(%d, %d) " % (node.data, node.height), end='')
        else:
            print("(%d, %d) " % (node.data, node.height), end='')

    def height(self, node):
        if node is None:
            return -1;
        else:
            return node.height

    def __updateHeight(self, node):
        if node is None:
            return;
        else:
            node.height = max(self.height(node.left), self.height(node.right)) + 1

    def findMin(self):
        minNode = self.__find_min(self.root)
        if minNode is None:
            return None
        else:
            return minNode.data

    def __findMin(self, node):
        if node is None:
            return None
        while node.left is not None:
            node = node.left
        return node

    def findMax(self):
        maxNode = self.__find_max(self.root)
        if maxNode is None:
            return None
        else:
            return minNode.data

    def __findMax(self, node):
        if node is None:
            return None
        while node.right is not None:
            node = node.right
        return node
    
    def find(self, data):
        node = self.root
        while node is not None:
            if data < node.data:
                node = node.left
            elif data > node.data:
                node = node.right
            else:
                return True
        return False

    def __path(self, data, node):
        path = []
        while node is not None:
            path.append(node)
            if data < node.data:
                node = node.left
            elif data > node.data:
                node = node.right
            else: # found
                break
        return path

    def dfs(self):
        stack = []
        node = self.root
        while node is not None:
            while node is not None:
                if node.right is not None:
                    stack.append(node.right)
                stack.append(node)
                node = node.left
            node = stack.pop()
            while node.right is None and len(stack) != 0:
                self.printNode(node)
                node = stack.pop()
            self.printNode(node)
            if len(stack) != 0:
                node = stack.pop()
            else:
                break
        print()
    
    def add(self, data):
        if self.root is None:
            self.root = self.Node(data)
        else:
            parent = None
            current = self.root
            while current is not None:
                if data < current.data:
                    parent = current
                    current = current.left
                elif data > current.data:
                    parent = current
                    current = current.right
                else: #duplicated, insert failed
                    return None 
            if data < parent.data:
                parent.left = self.Node(data)
            else:
                parent.right = self.Node(data)
        self.__balancePath(data)
        return data

    def __balancePath(self, data):
        path = self.__path(data, self.root)
        for i in range(len(path)-1, -1, -1):
            node = path[i]
            parent = None
            if node is not self.root:
                parent = path[i-1]
            self.__updateHeight(node)
            if self.height(node.left) - self.height(node.right) > 1:
                if self.height(node.left.left) > self.height(node.left.right):
                    self.__rotateLeft(node, parent)
                else:
                    self.__doubleRotateLeft(node, parent)
            elif self.height(node.right) - self.height(node.left) > 1:
                if self.height(node.right.right) > self.height(node.right.left):
                    self.__rotateRight(node, parent)
                else:
                    self.__doubleRotateRight(node, parent)

    def __rotateLeft(self, node, parent):
        print("L: " + str(node.data))
        leftNode = node.left
        node.left = leftNode.right
        leftNode.right = node
        self.__updateHeight(node)
        self.__updateHeight(leftNode)
        if parent is not None:
            if node.data < parent.data:
                parent.left = leftNode
            else:
                parent.right = leftNode
        else:
            self.root = leftNode

    def __rotateRight(self, node, parent):
        print("R: " + str(node.data))
        rightNode = node.right
        node.right = rightNode.left
        rightNode.left = node
        self.__updateHeight(node)
        self.__updateHeight(rightNode)
        if parent is not None:
            if node.data < parent.data:
                parent.left = rightNode
            else:
                parent.right = rightNode
        else:
            self.root = rightNode

    def __doubleRotateLeft(self, node, parent):
        print("DL: " + str(node.data))
        self.__rotateRight(node.left, node)
        self.__rotateLeft(node, parent)

    def __doubleRotateRight(self, node, parent):
        print("DR: " + str(node.data))
        self.__rotateLeft(node.right, node)
        self.__rotateRight(node, parent)

    def remove(self, data):
        parent = None
        current = self.root
        while current is not None:
            if data < current.data:
                parent = current
                current = current.left
            elif data > current.data:
                parent = current
                current = current.right
            else:
                break
        if current is None:
            return None # no such data
        elif current.right is None:
            if parent is None:
                self.root = current.left
            elif current.data < parent.data:
                parent.left = current.left
            else:
                parent.right = current.left
            self.__balancePath(parent.data)
        else:
            parentOfSmallestInRight = current
            smallestInRight = current.right

            while smallestInRight.left is not None:
                parentOfSmallestInRight = smallestInRight
                smallestInRight = smallestInRight.left
            current.data = smallestInRight.data
            if parentOfSmallestInRight.left is smallestInRight:
                parentOfSmallestInRight.left = smallestInRight.right
            else:
                parentOfSmallestInRight.right = smallestInRight.right
            self.__balancePath(parentOfSmallestInRight.data)
        return data

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
print("remove " + str(t.remove(1)))
t.dfs()
print("remove " + str(t.remove(3)))
t.dfs()

        


