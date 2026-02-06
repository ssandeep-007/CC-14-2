class Node:
    def __init__(self,x):
        self.data=x
        self.left=None
        self.right=None

class BST:
    def __init__(self):
        self.root=None

    def insert(self,data):
        if self.root is None:
            self.root= Node(data)
        else:
            self.insertRecursion(self.root,data)
    def insertRecursion(self,node,data):
        if data<node.data:
            if node.left is None:
                node.left=Node(data)
            else:
                self.insertRecursion(node.left,data)
        else:
            if node.right is None:
                node.right=Node(data)
            else:
                self.insertRecursion(node.right,data)
    
    def inorder(self,node):
        if node is None:
            return
        self.inorder(node.left)
        print(node.data,end=' ')
        self.inorder(node.right)


if __name__=="__main__":
    line1=list(map(int,input().split()))
    tree= BST()
    for x in line1:
        if x==-1:
            break
        tree.insert(x)
    tree.inorder(tree.root)



