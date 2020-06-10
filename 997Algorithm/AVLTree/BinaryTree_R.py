class BinaryTree:
    class Node:
        def __init__(self, data):
            self.data = data
            self.left = self.right = None

    def __init__(self):
        self.root = None

    def dfs(self):
        self.__dfs(self.root)
        print()

    def __dfs(self, node):
        if node is not None:
            self.__dfs(node.left)
            if node is self.root:
                print('R(' + str(node.data) + ') ', end='')
            else:
                print('(' + str(node.data) + ') ', end='')
            self.__dfs(node.right)
    
    def add(self, data):
        self.root = self.__add(data, self.root)

    def __add(self, data, node):
        if node is None:
            return self.Node(data)
        elif data < node.data:
            node.left = self.__add(data, node.left)
        elif data > node.data:
            node.right = self.__add(data, node.right)
        return node

    def remove(self, data):
        self.root = self.__remove(data, self.root)

    def __remove(self, data, node):
        if node is None:
            return None
        elif data < node.data:
            node.left = self.__remove(data, node.left)
        elif data > node.data:
            node.right = self.__remove(data, node.right)
        # data found in node
        elif node.left is not None and node.right is not None:
            node.data = self.__find_min(node.right).data
            node.right = self.__remove(node.data, node.right)
        elif node.left is not None:
            node = node.left
        else:
            node = node.right
        return node

    def find(self, data):
        return self.__find(data, self.root)

    def __find(self, data, node):
        if node is None:
            return False
        elif data < node.data:
            return self.__find(data, node.left)
        elif data > node.data:
            return self.__find(data, node.right)
        else:
            return True

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
            return None
        elif node.right is None:
            return node
        else:
            return self.__find_max(node.right)


bt = BinaryTree()
bt.add(5)
bt.add(3)
bt.add(8)
bt.add(1)
bt.add(10)
bt.dfs()
print(bt.find_min())
print(bt.find_max())
print(bt.find(0))
bt.remove(3)
bt.dfs()

