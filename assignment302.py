#Shifa Mehreen
#121910313005

#Concatenating arrays

def array_input():
	#length of array
	n = int(input("Enter length of an array: "))

	a=[] #declaring empty array

	#taking input from user for elements
	print("Enter elements: ")
	for i in range(0,n):
		k = int(input())
		a.append(k) #adding elements
		
	return a

#array1
a1 = array_input()
#array2
a2 = array_input()

#printing array
print("Array1: ",a1)
print("Array2: ",a2)

#adding elements into array3
a3 = a1+a2

#Sorting the new array: a3
for l in range(0,len(a3)):
	for m in range(l+1,len(a3)):
		#checking
		if a3[l] > a3[m]:
			#swapping
			temp = a3[l]
			a3[l] = a3[m]
			a3[m] = temp

#output
print("New Array is: ",a3)

