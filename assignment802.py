#Shifa Mehreen
#121910313005

#Identify the biggest and smallest key in a doubly linked list containing integers.
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
#finding largest and smallest
	def maxandminNodes(self):
		cur = self.head
		large = self.head.data
		small = self.head.data
		while cur:
			if cur.data > large:
				large = cur.data

			if cur.data < small:
				small = cur.data

			cur = cur.next
		print("Largest element is: ",large)
		print("Smallest node is: ",small)

#initialization
DLL = LinkedList()

#creating nodes and adding it to the lnked list
DLL.head = node(10) # head ==> 10
DLL.head.next = node(20) # 10 --> 20
DLL.head.next.next = node(30) # 10 --> 20 --> 30

#function calling
DLL.display()
DLL.maxandminNodes()