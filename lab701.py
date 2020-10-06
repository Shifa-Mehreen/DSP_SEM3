#Shifa Mehreen
#121910313005

#deleting middle node from linked list

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
	#deleting node other than first node function
	def deleteNode(self,data):
		temp = self.head
		pre_node = None #previous node variable assignment
		while temp:
			if temp.data == data:
				n = temp.next
				temp.next = None
				pre_node.next = n
			pre_node = temp
			temp = temp.next
		#if key is not in the list
		else:
			print("Error!! Enter correct key!")

LL = LinkedList()
n = int(input("Enter number of elements: "))
print("Enter elements: ")
for i in range(n):
	k = int(input())
	LL.append(k)

print("Before: ")
LL.display()

v = int(input("Element to be deleted: "))
LL.deleteNode(v)
print("New: ")
LL.display()


				



