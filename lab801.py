#Shifa Mehreen
#121910313005

#Create a doubly linked list
#node class
class node:
	#constructor
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

#printing list
	def display(self):
		ele = []
		cur = self.head
		while cur:
			ele.append(cur.data)
			cur = cur.next
		print("Doubly LinkedList: ",ele)

#initialization
DLL = LinkedList()

#creating nodes and adding it to the lnked list
DLL.head = node(10) # head ==> 10
DLL.head.next = node(20) # 10 --> 20
DLL.head.next.next = node(30) # 10 --> 20 --> 30

#function calling
DLL.display()


