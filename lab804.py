#Shifa Mehreen
#121910313005

#Insert Node at a particular position
#node class
class node:
	def __init__(self,data):
		self.data = data
		self.prev = None
		self.next = None
#linkedlist class
class LinkedList:
	def __init__(self):
		#initialization
		self.head = None
	#inserting node in the middle of the list
	def atPosition(self,pre,data):
		new_node = node(data)
		if self.head == None:
			self.head = new_node
		else:
			cur = self.head
			while cur:
				if cur.data == pre:
					n = cur.next
					cur.next = new_node
					new_node.next = n
					new_node.prev = cur
				cur = cur.next
	#printing elements
	def display(self):
		ele = []
		cur = self.head
		while cur:
			ele.append(cur.data)
			cur = cur.next
		print("Doubly Linked List: ",ele)

#linked list creation
DLL = LinkedList()

#adding nodes
DLL.head = node(10) # head ==> 10
DLL.head.next = node(20) # 10 --> 20
DLL.head.next.next = node(30) # 10 --> 20 --> 30
DLL.atPosition(20,5) # 10 --> 20 (pre node) --> 5 --> 30
DLL.atPosition(10,4) # 10 (pre node) --> 4 -->20 --> 5 -->30

#function calling
DLL.display()