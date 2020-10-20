#Shifa Mehreen
#121910313005

#Insert Node at begining
#node class
class node:
	def __init__(self,data):
		#instances
		self.data = data
		self.prev = None
		self.next = None
#linkedlist class		
class LinkedList:
	def __init__(self):
		#initialization
		self.head = None
	#adding nodes at front
	def prepend(self,data):
		new_node = node(data)
		if self.head == None:
			self.head = new_node
		else:
			self.head.prev = new_node
			new_node.next = self.head
			new_node.prev = None
			self.head = new_node
	#printing nodes
	def display(self):
		ele = []
		cur = self.head
		while cur:
			ele.append(cur.data)
			cur = cur.next
		print("Doubly LinkedList: ",ele)

#creating a linked list
DLL = LinkedList()

#adding nodes to list
DLL.head = node(10)  # head ==> 10
DLL.prepend(20) # 20 --> 10
DLL.prepend(30) # 30 --> 20 --> 10

#function calling
DLL.display()

