#Shifa Mehreen
#121910313005

#Delete a Node at Beginning, at Ending and at a given Position
#node class
class node:
	def __init__(self,data):
		self.data = data
		self.prev = None
		self.next = None

#linkedlist class
class LinkedList:
	def __init__(self):
		self.head = None
	#appending nodes
	def append(self,data):
		new_node = node(data)
		cur = self.head
		if self.head == None:
			self.head = new_node
		else:
			while cur.next:
				cur = cur.next
			cur.next = new_node
			new_node.prev = cur

#deleting a node at a particular position
	def deleteANode(self,data):
		cur = self.head
		while cur:
			#if data is head data
			if cur.data == data and cur == self.head:
				#if there are elements after head node
				if cur.next != None:
					n = cur.next
					cur.next = None
					n.prev = None
					self.head = n
					return
				#if there are no elements after head node
				else:
					cur = None
					self.head = None
					return
			#if data is other than head data
			elif cur.data == data:
				m = cur.next
				n = cur.prev
				cur.next = None
				cur.prev = None
				n.next = m
				return
				
			cur = cur.next #updating

		#if data not found
		else:
			print("no such data found!")
	
	#printing elements
	def display(self):
		ele = []
		cur = self.head
		while cur:
			ele.append(cur.data)
			cur = cur.next
		print("Doubly LinkedList: ",ele)

#creation of a linked list
DLL = LinkedList()

#adding elements
n = int(input("Enter no'of elements: "))
for i in range(n):
	k = int(input())
	DLL.append(k)

print("Before:")
DLL.display()

#taking in element that is to be deleted
x = int(input("Enter element to be deleted: "))
DLL.deleteANode(x)

print("After: ")
DLL.display()









