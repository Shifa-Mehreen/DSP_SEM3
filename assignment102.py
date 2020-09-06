#printing primes

#input
x = int(input("Enter a limit: "))

#logic

#prime : has factors 1 and itself

def prime(n): #creating a function
	count = 0
	for i in range(1,n+1): 
		if n%i == 0:
			count = count + 1
	if count == 2: 
		return True
	else: 
		return False #returns a boolean value

#printing uptil a limit
for n in range(1,x+1):
	if prime(n) is True:
		print(n)


