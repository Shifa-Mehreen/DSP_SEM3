#Shifa Mehreen
#121910313005

#Implement PUSH operation subject to exception in Stack

class Stack:
	def __init__(self):
		self.stack = []

	def push(self,data,n):
		if len(self.stack) < n:
			print("Pushing",data,"into stack")
			self.stack.append(data)
			return
		else:
			print("Exception: OVERFLOW, cant push",data,"into stack") #when len exceeds n 
		return

	def displayStack(self):
		print("Stack: ")
		for i in self.stack:
			print(i, end=" ")
		return

s = Stack()

n = int(input("Enter size: "))
s.push(10,n)
s.push(20,n)
s.push(30,n)
s.push(40,n)
s.push(50,n)
s.push(60,n)

s.displayStack()

