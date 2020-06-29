class AVLTree:
    class Node:
        def __init__(self, data):
            self.data = data
            self.left = self.right = None
            self.height = 0 #新的属性，说明节点的高度

    def __init__(self):
        self.root = None

    def height(self, node): #返回node节点的高度
        if node is None:
            return -1
        else:
            return node.height

    #如果node的左或右子树高度变了，就调用这个函数更新它的高度
    def __updateHeight(self, node): 
        if node is None:
            return -1
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
        if node is not None:
            self.__dfs(node.left)
            self.printNode(node)
            self.__dfs(node.right)

    def findMin(self):
        return self.__findMin(self.root).data

    def __findMin(self, node):
        if node is None:
            return None
        elif node.left is None:
            return node
        else: #左子树非空
            return self.__findMin(node.left) #递归

    def findMax(self):
        return self.__findMax(self.root).data

    def __findMax(self, node):
        if node is None:
            return None
        elif node.right is None:
            return node
        else:
            return self.__findMax(node.right)

    def add(self, data):
        self.root = self.__add(data, self.root) #添加data到以root为根的树上

    def __add(self, data, node):
        if node is None:
            return self.Node(data)
        elif data < node.data:
            #将data添加到左子树上，然后考虑是否要旋转
            node.left = self.__add(data, node.left) #递归地添加
            if self.height(node.left) - self.height(node.right) > 1:
                if data < node.left.data: #添加到了左子树的左边
                    node = self.__rotateLeft(node) #左旋
                else:
                    node = self.__doubleRotateLeft(node) #左双旋
        elif data > node.data:
            #将data添加到右子树上，然后考虑是否要旋转
            node.right = self.__add(data, node.right)
            if self.height(node.right) - self.height(node.left) > 1:
                if data > node.right.data:
                    node = self.__rotateRight(node) #右旋
                else:
                    node = self.__doubleRotateRight(node) #右双旋
        #else: 重复的节点，不做操作
        self.__updateHeight(node)
        return node #返回添加完成后，子树的根节点

    def __rotateLeft(self, node):
        leftNode = node.left
        node.left = leftNode.right #把left的右子树挂到root的左边
        leftNode.right = node #让原root作为left的右子树
        self.__updateHeight(node) #先更新原root的高度
        self.__updateHeight(leftNode)
        return leftNode

    def __rotateRight(self, node):
        #是__rotateLeft的镜像操作
        rightNode = node.right
        node.right = rightNode.left
        rightNode.left = node
        self.__updateHeight(node)
        self.__updateHeight(rightNode)
        return rightNode

    def __doubleRotateLeft(self, node):
        #1 在left上执行右旋，更新left
        node.left = self.__rotateRight(node.left)
        #2 在root上执行左旋，返回新的根
        return self.__rotateLeft(node)

    def __doubleRotateRight(self, node):
        #是__doubleRotateLeft的镜像操作
        node.right = self.__rotateLeft(node.right)
        return self.__rotateRight(node)
    
    def remove(self, data):
        stack = []
        self.root = self.__remove(data, self.root, stack)
        lastNode = stack[len(stack)-1]
        if lastNode is not None and lastNode.data == data: #有真正删除
            #依次解决这些节点可能存在的平衡问题
            for i in range(len(stack)-2, -1, -1):
                node = stack[i]
                isRoot = False
                if node is self.root:
                    isRoot = True
                if self.height(node.left) - self.height(node.right) > 1:
                    if self.height(node.left.left) > self.height(node.left.right):
                        node = self.__rotateLeft(node)
                    else:
                        node = self.__doubleRotateLeft(node)
                elif self.height(node.right) - self.height(node.left) > 1:
                    if self.height(node.right.right) > self.height(node.right.left):
                        node = self.__rotateRight(node)
                    else:
                        node = self.__doubleRotateRight(node)
                if isRoot:
                    self.root = node
                else:
                    parent = stack[i-1]
                    if node.data < parent.data:
                        parent.left = node
                    else:
                        parent.right = node


    def __remove(self, data, node, stack):
        stack.append(node) #将访问到的节点压栈
        if node is None:
            return None
        elif data < node.data:
            node.left = self.__remove(data, node.left, stack)
        elif data > node.data:
            node.right = self.__remove(data, node.right, stack)
        elif node.left is not None and node.right is not None:
            node.data = self.__findMin(node.right).data
            node.right = self.__remove(node.data, node.right, stack)
        elif node.left is not None:
            node = node.left
        else:
            node = node.right
        self.__updateHeight(node)
        return node

tree = AVLTree()
tree.add(5)
tree.add(3)
tree.add(7)
tree.add(8)
#tree.root = AVLTree.Node(5)
#tree.root.left = AVLTree.Node(3)
#tree.root.right = AVLTree.Node(7)
tree.dfs()
#print(tree.findMin())
#print(tree.findMax())
tree.remove(3)
tree.dfs()
