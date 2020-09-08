#121910313005
#Shifa Mehreen

#reversing an array

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

#array2
l = len(a1) #length of array:function - len() 

a2 = [None]*len(a1) #declaring another array2 
                    #with same length as array1

for i in range(0,n):
	a2[i] = a1[l-i-1] #logic to reverse an array

print("Reverse of Array is: ",a2) #printing
	