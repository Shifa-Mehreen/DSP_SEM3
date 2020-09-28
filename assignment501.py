#Shifa Mehreen
#121910313005

#Binary search with user defined function
#no recurrsion

#input
arr = [22,53,46,90,12]
print("Array is: ",arr)

#function
def binarysearch_array(a):
	a.sort() 
	print("Sorted array is: ",a)

#search element
	x = int(input("Enter search element: "))

	# taking ranges
	loc =0
	low = 0
	high = len(a) - 1
	mid = (low+high)//2

	#checking with mid value
	if a[mid] == x:
		loc = mid
		f = 1

	#checking with elements lesser than the mid value
	elif x < a[mid]:
		for i in range(low,mid):
			if a[i] == x:
				loc = i
				f = 1
				break

	#checking with elements greater than the mid value
	elif x > a[mid]:
		for i in range(mid,high+1):
			if a[i] == x:
				loc = i
				f = 1
				break

    #output
    #if found
    if f == 1:
        print("Element",x,"is found at index",loc)
    #if not found
    else:
        print("Element not found!!")
        
#function calling
binarysearch_array(arr)