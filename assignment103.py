#input
n = int(input('Enter a number: '))

original_n = n
m = n
#sum of digits of a number

#logic
sum = 0
x = 0

while n>0:

 i = n % 10  #reminder
 x = x + 1  #no'of digits
 sum = sum + i
 n = n//10  #quotient as a whole number (floor division)

print(sum)
print('No. of digits in the given number are: ',x)

#armstrong number

sum1 = 0

while m>0:

	k = m % 10
	pow = k**x #power: k-base x-exponent
	sum1 = sum1 + pow
	m = m//10

#decision making
if original_n == sum1:
	print("It is an Armstrong Number!")
else:
	print("It is not an Armstrong Number!!")
