#121910313005
#Shifa Mehreen

#Create a binary tree and insert atleast 12 nodes into it
#with user input values
#i.e, at run time initialization

class Node:
	def __init__(self,data):
		self.data = data
		self.left = None
		self.right = None

class BinaryTree:
	def __init__(self):
		self.root = None

	def insertNodes(self,data):
		#binary search tree
		if self.root is None:
			self.root = Node(data)
			return
		cur = self.root
		while cur:
			if cur.data > data: #left nodes must be smaller
				if cur.left:  
					cur = cur.left
				else:
					cur.left = Node(data)
					break
			else:
				if cur.right: #right nodes must be bigger
				              #than left ones
					cur = cur.right
				else:
					cur.right = Node(data)
					break

	def printNodes(self,node):
		print(node.data, end = " ")
		if node.left: self.printNodes(node.left)
		if node.right: self.printNodes(node.right)

B = BinaryTree()

n = int(input("Enter no.of nodes: "))
print("Enter node values")
for i in range(n):
	k = int(input())
	B.insertNodes(k)

print("Tree: ")
B.printNodes(B.root)






