#Shifa Mehreen
#121910313005

#Implement stack operation through singly linked list

#node class
class Node:
	def __init__(self,data):
		#instances
		self.data = data
		self.next = None
#stack class as linked list
class Stack:
	def __init__(self):
		#initialization
		self.head = None
		self.tail = None
	#adding nodes
	def push(self,data):
		new_node = Node(data)
		if self.head is None:
			self.head = new_node
			self.tail = new_node
		else:
			self.tail.next = new_node
			self.tail = new_node
	#printing the last in node
	def peek(self):
		l = self.tail.data
		return l
	#deleteing the last in node
	def pop(self):
		if self.head is None:
			print("UNDERFLOW")
		else:
			prev = None
			cur = self.head
			while cur:
				prev = cur
				cur = cur.next #iterating till end of satck
			#deleting last node in stack
				if cur == self.tail:
						prev.next = None
						cur = None
						self.tail = prev
	#printing stack
	def displayStack(self):
		print("Stack: ")
		temp = self.head
		while temp:
			print(temp.data, end=" ")
			temp = temp.next
		print()
	
s=Stack()
#function calling
s.push(10)
s.push(20)
s.push(30)
s.push(40)
s.displayStack()
print(s.peek())
s.pop()
s.displayStack()

