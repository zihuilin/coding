class BinaryTree:
    class Node:
        def __init__(self, data):
            self.data = data
            self.left = self.right = None

    def __init__(self):
        self.root = None

    def printNode(self, node):
        if node is self.root:
            print('R(' + str(node.data) + ') ', end='')
        else:
            print('(' + str(node.data) + ') ', end='')

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
            if len(stack) == 0:
                break
            else:
                node = stack.pop()
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
                else:
                    return None # insert failed
            if data < parent.data:
                parent.left = self.Node(data)
            else:
                parent.right = self.Node(data)
        return data

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
            return None # remove failed
        elif current.right is None:
            if parent is None:
                self.root = current.left
            elif current.data < parent.data:
                parent.left = current.left
            else:
                parent.right = current.left
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
        return data

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

    def find_min(self):
        if self.root is None:
            return None
        else:
            node = self.root
            while node.left is not None:
                node = node.left
            return node.data

    def find_max(self):
        if self.root is None:
            return None
        else:
            node = self.root
            while node.right is not None:
                node = node.right
            return node.data

bt = BinaryTree()
bt.add(5)
bt.add(3)
bt.add(8)
bt.add(2)
bt.add(1)
bt.add(7)
bt.add(9)
bt.dfs()
bt.remove(8)
print(bt.find(3))
print(bt.find_min())
print(bt.find_max())
bt.dfs()

        

