class BinaryTree:  # 二叉树
    class Node:    # 内部类：树中的节点
        def __init__(self, data):
            self.data = data
            self.left = self.right = None #初始化时左右子树为空

    def __init__(self):
        self.root = None

    def printNode(self, node):
        if node is not None:
            if node is self.root:
                print("R(" + str(node.data) + ") ", end='')
            else:
                print("(" + str(node.data) + ") ", end='')

    def dfs(self):
        self.__dfs(self.root) #从根开始dfs
        print()

    def __dfs(self, node): #深搜：从node开始，左中右
        if node is not None: #节点不为空
            self.__dfs(node.left)
            self.printNode(node)
            self.__dfs(node.right)
        #出口：节点为空，不必搜

    def find_min(self):
        if self.root is None: #空树，不必搜索
            return None
        else:
            return self.__find_min(self.root).data

    def __find_min(self, node): #搜索node子树上最小的节点
        if node is None: #节点为空，子树就为空
            return None  #不必搜索
        elif node.left is None: #没有左子树
            return node #那么这个节点就是最小的节点
        else: # 如果有左子树
            return self.__find_min(node.left) #递归地在左子树上搜索最小的节点

    def find_max(self):
        if self.root is None: #空树，不必搜索
            return None
        else:
            return self.__find_max(self.root).data

    def __find_max(self, node): #搜索node子树上最大的节点
        if node is None: #节点为空，子树就为空
            return None  #不必搜索
        elif node.right is None: #没有右子树
            return node #那么这个节点就是最大的节点
        else: # 如果有右子树
            return self.__find_max(node.right) #递归地在右子树上搜索最小的节点

    def find(self, data):
        return self.__find(data, self.root) #从根开始，搜索data

    def __find(self, data, node): #在node子树上搜索data数据
        if node is None: #空子树
            return False #找不到
        if data < node.data:
            return self.__find(data, node.left) #递归地在左子树上搜索data
        elif data > node.data:
            return self.__find(data, node.right) #递归地在右子树上搜索data
        else: #等于data!!
            return True #找到了！

    # 公开的add函数
    def add(self, data):
        if self.root is None: #本来这是个空树
            self.root = self.Node(data)
        else:
            self.__add(data, self.root) #添加data到以root为根的树上
    
    def __add(self, data, node): #添加data到node子树，并返回添加完成后node子树的根
        if node is None: #要添加data到空树上
            node = self.Node(data) #添加完成后，这个树就只有data这一个节点
        elif data < node.data: #因为要添加的data比当前节点小，
            node.left = self.__add(data, node.left) #递归地添加data到node的左子树上
        elif data > node.data: #因为要添加的data比当前节点大，
            node.right = self.__add(data, node.right) #递归地添加data到node的左子树上
        #最后,返回这个子树的根
        return node

    def remove(self, data):
        self.root = self.__remove(data, self.root)

    def __remove(self, data, node):
        if node is None: #在空树上删除data
            return None #删除完了，还是空树
        elif data < node.data: #要删除的数据比根小
            node.left = self.__remove(data, node.left)#在左子树上删除
        elif data > node.data: #要删除的数据比根大
            node.right = self.__remove(data, node.right)#在右子树上删除
        #下面就是data 等于 node.data的情况了
        elif node.left is not None and node.right is not None: #既有左子树，也有右子树
            node.data = self.__find_min(node.right).data #将node右子树上最小节点的数据，存放到node里
            node.right = self.__remove(node.data, node.right) #将右子树里最小的节点删除（递归）
        elif node.left is not None: #右子树一定是没有的
            node = node.left
        else: #有右子树，没有左子树,以及左右都没有
            node = node.right
        return node #返回删除完后，新的树的根


tree = BinaryTree()
'''
tree.root = BinaryTree.Node(5)
tree.root.left = BinaryTree.Node(3)
tree.root.right = BinaryTree.Node(7)
'''
tree.add(5)
tree.add(3)
tree.add(7)
tree.dfs()
print(tree.find_min())
print(tree.find_max())
print(tree.find(9))
tree.add(1)
tree.add(4)
tree.add(6)
tree.add(8)
tree.add(2)
tree.add(0)
tree.add(9)

tree.dfs()
tree.remove(5)
tree.dfs()
tree.remove(3)
tree.dfs()

tree.remove(0)
tree.dfs()



