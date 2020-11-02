#Shifa Mehreen
#121910313005

#POP a specific element from a stack

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

	def popelement(self,data):
		#searching for tht element in stack
		#and removing it
		if x in self.stack:
			self.stack.remove(x)
		else:
			print("Element not found!")

	def displayStack(self):
		if len(self.stack) >0:
			print("Stack: ")
			for i in self.stack:
				print(i, end=" ")
			print()
			return
		else:
			print("Empty Stack")

s = Stack()
n = int(input("Enter Size: "))
print("Enter elements: ")
for i in range(n):
	k = int(input())
	s.push(k,n)
s.displayStack()

x= int(input("Enter element you want to delete: "))
s.popelement(x)
s.displayStack()