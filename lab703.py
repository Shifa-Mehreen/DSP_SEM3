#Shifa Mehreen
#121910313005
#Deleting Last node

#Nose Class
class node:
	def __init__(self,data):
		self.data = data
		self.next = None
#Linked list class
class LinkedList:
	def __init__(self):
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
	#deleting last node function
	def deleteLastNode(self):
		temp = self.head
		pre_node = None
		print("Tail Node:" self.tail.data)
		while temp:
			if temp == self.tail:				
				pre_node.next = None
			pre_node = temp
			temp = temp.next

LL = LinkedList()
n = int(input("Enter number of elements: "))
print("Enter elements: ")
for i in range(n):
	k = int(input())
	LL.append(k)

print("Before: ")
LL.display()

LL.deleteLastNode()
print("New: ")
LL.display()
