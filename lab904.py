#Shifa Mehreen
#121910313005

#Stack Operations

class Stack:
	def __init__(self):
		self.stack = []

	def push(self,data,n):
		if len(self.stack) < n:
			self.stack.append(data)
			return
		else:
			print("OVERFLOW")
			return

	def pop(self):
		if len(self.stack) > 0:
			x = self.stack[-1]
			print("pop element",x)
			self.stack.pop()
		else:
			print("Exception: UNDERFLOW")

	def popelement(self,data):
		if x in self.stack:
			self.stack.remove(x)
		else:
			print("Element not found!")

	def peek(self):
		x = self.stack[-1]
		print("Last element: ",x)

	def displayStack(self):
		if len(self.stack) >0:
			print("Stack: ")
			for i in self.stack:
				print(i, end=" ")
			print()
			return
		else:
			print("Empty Stack")

t = True
s = Stack()
n = int(input("Enter Size: "))
while t:
	print("1.PUSH 2.POP 3.POP a specific element 4.PEEK 5.DISPLAY 6.EXIT")
	i = int(input("Enter number for the specific operation to be performed: "))
	if i == 1:
		s.push(int(input("Enter element: ")),n)
	elif i == 2:
		s.pop()
	elif i == 3:
		x= int(input("Enter element you want to delete: "))
		s.popelement(x)
	elif i == 4:
		s.peek()
	elif i == 5:
		s.displayStack()
	elif i == 6:
		t = False
	else:
		print("Enter Valid Input!")