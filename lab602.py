#Shifa Mehreen
#121910313005

#Linked lists with dynamic inputs

#Node class for each element
class node:
	#parametarized constructor
	def __init__(self,data=None):
		self.data=data
		self.next=None

#linked list class to join other elements
class linkedlist:
	#default constructor
	def __init__(self):
		#intializing head and tail node
		self.head = None
		self.tail = None

	#function to add elements
	def append(self,data):
		if self.tail == None:
			self.head = node(data)
			self.tail = self.head
		else:
			self.tail.next = node(data)
			self.tail = self.tail.next
		

	#function to display elements
	def display(self):
		ele = []
		cur_node = self.head
		while cur_node != None:
			ele.append(cur_node.data)
			cur_node = cur_node.next
		print ("Given Linked List:" ,ele)

LL = linkedlist()
n = int(input("No'of elements: "))
print("Enter elements: ")
for i in range(n):
	k = int(input())
	LL.append(k)
LL.display()
