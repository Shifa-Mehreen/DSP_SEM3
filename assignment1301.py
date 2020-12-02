#121910313005
#Shifa Mehreen

#Create a tree with at least 12 nodes 
#and perform in-order, pre-order, and post-order traversal 
#and print the values present at the nodes.


class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
class BinaryTree:
    def __init__(self):
        self.root=None

    def insertNodes(self,data):
        node = Node(data)
        q = []
        if self.root == None:
            self.root = node
        else:
            q.append(self.root)

        while len(q) != 0:
            n = q.pop(0)
            if n.left == None:
                n.left = node
                break
            else:
                q.append(n.left)

            if n.right == None:
                if n.right == None:
                    n.right = node
                    break
                else:
                    q.append(n.right)

    def PrintTree(self,node):
        if node.left: self.PrintTree(node.left)
        print(node.data, end=" ")
        if node.right: self.PrintTree(node.right)


    def PreOrder(self,node):
        print(node.data, end=" ")
        if node.left: self.PreOrder(node.left)
        if node.right: self.PreOrder(node.right)

    def InOrder(self,node):
        if node.left: self.InOrder(node.left)
        print(node.data, end=" ")
        if node.right: self.InOrder(node.right)

    def PostOrder(self,node):
        if node.left: self.PostOrder(node.left)
        if node.right: self.PostOrder(node.right)
        print(node.data, end=" ")

B = BinaryTree()
n = int(input("Enter no.of nodes: "))
print("Enter node values")
for i in range(n):
    k = int(input())
    B.insertNodes(k)

print("Tree:")
B.PrintTree(B.root)
print("\n")
print("Preorder Traversal ")
B.PreOrder(B.root)
print("\n")
print("Inorder Traversal ")
B.InOrder(B.root)
print("\n")
print("Postorder Traversal ")
B.PostOrder(B.root)