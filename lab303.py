#121910313005
#Shifa Mehreen

#removing duplicates

#array1
#length of array1
n = int(input("Enter length of an array: "))

a1=[] #declaring empty array

#taking input from user
print("Enter elements: ")
for i in range(0,n):
	k = int(input())
	a1.append(k) #adding elements
	
print("Array is: ",a1) 

#function to remove duplicates
def remove(a1):
	a2=[]
	for num in a1:
		if num not in a2:
			a2.append(num)
	return a2

print("New Array is: ",remove(a1))

