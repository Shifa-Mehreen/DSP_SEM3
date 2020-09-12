#Shifa Mehreen
#121910313005

#Searching an element from an array

#length input
n = int(input("Enter length: "))

#array elements input
print("Enter elements: ")
a = []
for i in range(0,n):
	k = int(input())
	a.append(k)

print(a)  #printing elements

#search function
def search(x):
	for i in range(0,n):
		if a[i] == x:
			loc = i #location of that element
			print("Found the search element:",x, "at the location:",i)
			break
	else:
		print("Search element:",x,"not found!")


#input for the search element
l = int(input("Enter the search element: "))

search(l) #calling the "search" function
