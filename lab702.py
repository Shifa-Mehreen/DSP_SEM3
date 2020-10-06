#Shifa Mehreen
#121910313005

#Deleting first node

#Node Class
class node:
	def __init__(self,data):
		self.data = data
		self.next = None
#Linked List Class
class LinkedList:
	def __init__(self):
		#initialization
		self.head = None
		self.tail = None
	#adding elements
	def append(self,data):
		new_node = node(data)
		if self.head == None or self.tail == None:
			self.head = new_node
			self.tail = new_node
		else:
			self.tail.next = new_node
			self.tail = new_node
	#printing elements
	def display(self):
		ele = []
		temp = self.head
		while temp:
			ele.append(temp.data)
			temp = temp.next
		print("Linked List: ",ele)
	#deleting first node function
	def deleteFirstNode(self):
		temp = self.head
		print("First Node: ",self.head.data)
		n = temp.next
		temp.next = None
		self.head = n

LL = LinkedList()
n = int(input("Enter number of elements: "))
print("Enter elements: ")
for i in range(n):
	k = int(input())
	LL.append(k)

print("Before: ")
LL.display()

LL.deleteFirstNode()
print("New: ")
LL.display()
