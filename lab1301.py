#121910313005
#Shifa Mehreen

#Create a Binary Tree with a single node

class Node:
	def __init__(self,data):
		self.data = data
		self.left = None
		self.right = None
class BinaryTree:
	def __init__(self):
		self.root = None

x = int(input("Enter Root Node value: "))

B = BinaryTree()
B.root = Node(x)

print("Tree : ")
print(B.root.data)
