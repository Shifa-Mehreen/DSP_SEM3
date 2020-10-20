#Shifa Mehreen
#121910313005

#Insert node at End
#node class
class node:
	def __init__(self,data):
		self.data = data
		self.prev = None
		self.next = None
#clinkedlist class		
class LinkedList:
	def __init__(self):
		#initialization
		self.head = None

	#adding node at end 
	def atEnd(self,data):
		new_node = node(data)

		if self.head == None:
			self.head = new_node
		else:
			cur = self.head
			while cur:
				if cur.next == None:
					cur.next = new_node
					new_node.next = None 
					new_node.prev = cur
				cur = cur.next

#printing elements
	def display(self):
		ele = []
		cur = self.head
		while cur:
			ele.append(cur.data)
			cur = cur.next
		print("Doubly LinkedList: ",ele)

DLL = LinkedList()

#adding nodes
DLL.head = node(10) # head ==> 10
DLL.head.next = node(20) # 10 --> 20
DLL.atEnd(30) # 10 -->20 --> 30
DLL.atEnd(40) # 10 -->20 --> 30 --> 40

#printing elements
DLL.display()

