#Shifa Mehreen
#121910313005

#Insert a Node in the middle
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

	#inserting the node at places other than the start or end node
	def AtMid(self,pre_node,data):
		new_node = node(data)
		temp = self.head #pointing variable
		while temp:
			if temp.data == pre_node: #checking for the prenode
				break
			temp = temp.next
		n = temp.next #storing next node
		temp.next = new_node
		new_node.next = n



LL = LinkedList()
n = int(input("Enter number of elements: "))
print("Enter elements: ")
for i in range(n):
	k = int(input())
	LL.append(k)

print("Before: ")
LL.display()


x = int(input("Enter previous node: "))
y = int(input("Enter element to be placed: "))
LL.AtMid(x,y)
print("New: ")
LL.display()






