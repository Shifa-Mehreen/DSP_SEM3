#Shifa Mehreen
#121910313005

#operations on array

#input of array

#length
print("Enter length: ")
n = int(input())

#elements input
print("Enter elements: ")
a = []
for i in range(0,n):
	k = int(input())
	a.append(k)

#display elements
def display_element():
	print("Array is: ",a)

#copy elements
def copy_element():
	a1 = a
	print("Copied array: ",a1)

#remove element
def remove_element():
	print("Enter the value of the element to be removed: ")
	x = int(input())
	a.remove(x)
	print("New Array: ",a)

##remove(): removes elements by value

#delete element
def delete_element():
	print("Enter the index of the element to be deleted: ")
	y = int(input())
	del a[y]
	print("New Array: ",a)

##del : deletes the number by index

#search element
def search_element():
	print("Enter the search element: ")
	l = int(input())
	for i in range(0,n):
		if a[i] == l:
			loc = i
			print("Element: ",l,"is found at index: ",loc)
			break
	else:
		print("Oops! Element not found!!")

#removing duplicates
def remove_duplicate_element():
	a1=[]
	for i in a:
		if i not in a1:
			a1.append(i)
	print("New Array is: ",a1)

#choices
print("Hey!!Choose: \n 1:to display \n 2:to copy \n 3:to remove \n 4:to delete \n 5:to search \n 6:array without duplicates")

print("Enter choice: ")
q = int(input())

#selection
if (q == 1):
	display_element()
elif (q == 2):
	copy_element()
elif (q == 3):
	remove_element()
elif (q == 4):
	delete_element()
elif (q == 5):
	search_element()
elif (q == 6):
	remove_duplicate_element()
else:
	print("Wrong choice!! Enter a right number from 1 to 5!")









