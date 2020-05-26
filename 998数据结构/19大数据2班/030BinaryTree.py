class BinaryTree:
    class Node:
        def __init__(self, d):
            self.data = d;
            self.left = None    #左后继
            self.right = None   #右后继

    def __init__(self):
        self.root = None

    def travel(self, n):
        if n != None:
            self.travel(n.left) #再看左后继
            print(n.data)  #(1)先看此节点
            self.travel(n.right) #再看右后继


tree = BinaryTree()
tree.root = BinaryTree.Node(5)
tree.root.left = BinaryTree.Node(3)
tree.root.left.left = BinaryTree.Node(1)
tree.root.left.right = BinaryTree.Node(4)
tree.root.right = BinaryTree.Node(7)
tree.root.right.left = BinaryTree.Node(6)
tree.root.right.right = BinaryTree.Node(8)

tree.travel(tree.root)
