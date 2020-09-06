#printing twin primes

#input
x = int(input("Enter a limit: "))

#logic

#prime function
def prime(n):
	count = 0
	for i in range(1,n+1):
		if n%i == 0:
			count = count + 1
	if count == 2:
		return True
	else:
		return False

#twin pimes: primes that differ by 2

#printing twin primes uptil a limit
for n in range(1,x+1):
	if prime(n) and prime(n+2) and ((n+2) <= x) is True:
		print(n,n+2)


#checking if n and n+2 are primes.
#and n+2 must satify the limit x, so it should be less than or equal to x.
#since all the 3 stmts must be satisfied, join them with 'and' opertor and check.


