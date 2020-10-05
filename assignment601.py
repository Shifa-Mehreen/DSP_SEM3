#Shifa Mehreen
#121910313005

#Insert a Node at the end
#Node Class
class node:
	def __init__(self,data):
		self.data = data
		self.next = None
#linkedlist Class
class LinkedList:
	def __init__(self):
		#initialization
		self.head = None
		self.tail = None

	#adding elements
	def append(self,data):
		new_node = node(data)
		#if empty
		if self.head == None and self.tail == None:
			self.head = new_node
			self.tail = new_node
		#if not empty
		else:
			self.tail.next = new_node
			self.tail = new_node

	#printing elements
	def display(self):
		ele = []
		cur = self.head #current pointing to head
		while cur:
			ele.append(cur.data)
			cur = cur.next #going to the next element
		print("Linked List: ",ele)

	#inserting at the end function
	#same as the append function
	def AtEnd(self,data):
		new_node = node(data)
		if self.head == None and self.tail == None:
			self.head = new_node
			self.tail = new_node
		else:
			self.tail.next = new_node
			self.tail = new_node

LL = LinkedList()
n = int(input("Enter number of elements: "))
print("Enter elements: ")
for i in range(n):
	k = int(input())
	LL.append(k)

print("Before: ")
LL.display()


print("Enter element to be placed end: ")
x = int(input())
LL.AtEnd(x)
print("New: ")
LL.display()






