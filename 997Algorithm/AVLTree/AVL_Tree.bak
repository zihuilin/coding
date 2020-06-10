class AVLTree:
    class AVLNode:
        def __init__(self, data):
            self.data = data
            self.left = None;
            self.right = None;
            self.height = 0;
        
        def __str__(self):
            return '(%d-%d)' %(self.data, self.height)

        def __eq__(self, other):
            return self.data == other.data

        def __le__(self, other):
            return self.data <= other.data

        def __ge__(self, other):
            return self.data >= other.data

        def __lt__(self, other):
            return self.data < other.data

        def __gt__(self, other):
            return self.data > other.data

    def __init__(self):
        self.root = None

    def height(self, node):
        if node is None:
            return -1
        else:
            return node.height

    def find_min(self):
        return self.__find_min_node(self.root).data

    def __find_min_node(self, node):
        if node is None:
            return None
        elif node.left is None:
            return node
        else:
            return self.__find_min_node(node.left)

    def find_max(self):
        return self.__find_max_node(self.root).data

    def __find_max_node(self, node):
        if node is None:
            return None
        elif node.right is None:
            return node
        else:
            return self.__find_max_node(node.right)

    def dfs(self):
        self.__dfs(self.root)
        print()

    def __dfs(self, node):
        if node is not None:
            self.__dfs(node.left)
            if node is self.root:
                print('R%s ' % node, end = '')
            else:
                print('%s ' % node, end = '')
            self.__dfs(node.right)


    def find(self, data):
        node = self.__find(data, self.root)
        if node is None:
            return None
        else:
            return node.data

    def __find(self, data, node):
        if node is None:
            return None
        elif data < node.data:
            return self.__find(data, node.left)
        elif data > node.data:
            return self._find(data, node.right)
        else:
            return node

    def insert(self, data):
        if self.root is None:
            self.root = self.AVLNode(data)
        else:
            self.__insert(data, self.root)

    def __insert_non_recursive(self, data, node):
        new_node = self.AVLNode(data)
        if node is None:
            return new_node
        else:
            p = node
            while True:
                if data < node.data:
                    if node.left is None:
                        node.left = new_node
                        break
                    else:
                        node = node.left
                elif data > node.data:
                    if node.right is None:
                        node.right = new_node
                        break
                    else:
                        node = node.right
                else:
                    break; # already have the same node

    def __insert(self, data, node):
        if node is None:
            return self.AVLNode(data)
        elif data < node.data:
            node.left = self.__insert(data, node.left)
        elif data > node.data:
            node.right = self.__insert(data, node.right)
        return node

    def delete(self, data):
        if self.root is None:
            return None
        elif data == self.root.data:
            self.root = self.__delete(data,self.root)
        else:
            self.__delete(data,self.root)

    def __delete(self, data, node):
        if node is None:
            return None
        if data < node.data:
            node.left = self.__delete(data, node.left)
        elif data > node.data:
            node.right = self.__delete(data, node.right)
        elif node.left is not None and node.right is not None:
            new_root = self.__find_min_node(node.right)
            print(new_root)
            new_root.right = self.__delete(new_root.data, node.right)
            new_root.left = node.left
            node = new_root
        else:
            if node.left is not None:
                node = node.left
            else:
                node = node.right
        return node

    def __delete_non_recursive(self, data, node):
        if node is None:
            return None
        pre = node       # parent
        tbd = node       # to be delete
        while tbd is not None and tbd.data != data:
            pre = tbd
            if data < tbd.data:
                tbd = tbd.left
            if data > tbd.data:
                tbd = tbd.right
        if tbd.left is None:
            new_root = tbd.right
        elif tbd.right is None:
            new_root = tbd.left
        else:
            new_root = self.__find_min_node(tbd.right)
            tbd.right = self.__delete_non_recursive(new_root.data, tbd.right)
            new_root.left = tbd.left
            new_root.right = tbd.right
        if tbd is pre:
            return new_root
        else:
            if tbd.data < pre.data:
                pre.left = new_root
            else:
                pre.right = new_root
            return node
            

tree = AVLTree()
tree.insert(5)
tree.insert(3)
tree.insert(8)
tree.insert(1)
print(tree.find(1))
print(tree.find_max())
tree.dfs()
tree.delete(5)
tree.dfs()
