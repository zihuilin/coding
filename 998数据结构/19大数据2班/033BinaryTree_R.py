class BinaryTree:
    class Node:
        def __init__(self, data):
            self.data = data
            self.left = self.right = None #左右子树都为空
    def __init__(self):
        self.root = None #空树

    def printNode(self, node):
        if node is not None:
            if node is self.root:
                print("R(" + str(node.data) + ") ", end='')
            else:
                print("(" + str(node.data) + ") ", end='')
    
    def dfs(self):
        self.__dfs(self.root)
        print() #回车

    def __dfs(self, node):  #在node子树上，从小到大遍历数据
        if node is not None:
            self.__dfs(node.left)
            self.printNode(node)
            self.__dfs(node.right)
        #隐藏了的出口： node is None，直接返回

    def findMin(self):
        if self.root is None:
            return None
        else:
            return self.__findMin(self.root).data

    def __findMin(self, node): #在node子树上搜索最小值所在的节点
        if node is None: #如果node子树为空
            return None
        elif node.left is None: #如果node没有左子树
            return node  #那么node上的数据就是最小的
        else: #有左子树
            return self.__findMin(node.left) #递归在左子树上搜索最小值

    def findMax(self):
        if self.root is None:
            return None
        else:
            return self.__findMax(self.root).data

    def __findMax(self, node):
        if node is None:
            return None
        elif node.right is None:
            return node
        else:
            return self.__findMax(node.right)

    def find(self, data):
        return self.__find(data, self.root) #从根开始，递归搜索data

    def __find(self, data, node): #在node子树上，搜索data，找到True，找不到False
        if node is None: #空子树
            return False #递归出口
        elif data < node.data: #要找的数据比node小
            return self.__find(data, node.left) #递归地在左子树上搜索
        elif data > node.data: #要找的数据比node大
            return self.__find(data, node.right) #递归地在右子树上搜索
        else: #data == node.data   -->>找到了！！
            return True
    
    def add(self,data):  #公开add方法，将data添加到树上
        self.root = self.__add(data, self.root) #包含self.root为None情况

    def __add(self, data, node): #在node子树上，添加data，并返回子树的根
        if node is None: #要添加数据的子树是空树
            node = self.Node(data) #递归出口：这个子树的根为data节点
        elif data < node.data:
            node.left = self.__add(data, node.left)#递归地将data添加到node的左子树上
        elif data > node.data:
            node.right = self.__add(data, node.right)#递归地将data添加到node的右子树上
        #最后，应该返回子树的根
        return node

tree = BinaryTree()
tree.add(5)
tree.add(3)
tree.add(7)
tree.dfs()
print(tree.find(9))
print(tree.findMin())
print(tree.findMax())

