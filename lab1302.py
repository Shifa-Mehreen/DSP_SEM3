#121910313005
#Shifa Mehreen

#Create a binary tree and insert atleast 12 nodes into it
#with compile time initialization

class Node:
	def __init__(self,data):
		self.data = data
		self.left = None
		self.right = None

class BinaryTree:
	def __init__(self):
		self.root = None

	def printNodes(self,root):
		q = []
		a = []
		if root == None:
			return
		if root != None:
			q.append(root)
		while len(q) > 0:
			a.append(q[0].data)
			node = q.pop(0)

			if node.left != None:
				q.append(node.left)
			if node.right != None:
				q.append(node.right)
		print ("Tree:",a)

B = BinaryTree()                                         #  1
B.root = Node(1)										# /   \
B.root.left = Node(2)							       # /     \
B.root.right = Node(3)                                # 2       3
B.root.left.left = Node(4)                           # / \     /  \
B.root.left.right = Node(5)                         # 4   5   10   9
B.root.left.left.left = Node(6)					   # / \     /  \
B.root.left.left.right = Node(7)				  # 6   7   11  12
B.root.left.left.left.left = Node(8)			 # /
B.root.right.right = Node(9)					# 8
B.root.right.left = Node(10)
B.root.right.left.left = Node(11)
B.root.right.left.right = Node(12)

B.printNodes(B.root)

