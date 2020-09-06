#perfect number or not

#input
n = int(input('Enter a number: '))

#ogic
sum = 0
for i in range(1,n):
	if n%i == 0:
		sum = sum + i

#perfect number: when sum of factors(excluding itself) is equal to the given number
if n == sum:
	print('It is a perfect number!')
else:
	print('It is not a perfect number!!')