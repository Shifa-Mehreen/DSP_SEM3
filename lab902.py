#Shifa Mehreen
#121910313005

#Implement POP operation subject to exception in Stack

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
			print("Exception: UNDERFLOW") #when there are no more elements left in
                                          #stack or if it is an empty stack
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

s.pop()
s.pop()
s.pop()
s.pop()
s.displayStack()




