#Shifa Mehreen
#121910313005

#linear search using functions

n = int(input("Enter no'of elements: "))
print("Enter elements: ")
a = []
for i in  range(0,n):
	k = int(input())
	a.append(k)

print("Array is: ",a)
		

def search_array(arr):
	x = int(input("Enter search element: "))

	loc = 0
	for i in range(0,len(a)):
		if arr[i] == x:
			loc = i
			print("Element",x,"is found at index",loc)
			break
	else:
		print("Element not found!!")

search_array(a)



