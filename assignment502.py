#Shifa Mehreen
#121910313005

#Binary search with user defined function and dynamic inputs
#with recurssion

#dynamic inputs
def array_input():
	n = int(input("Enter no'of elements: "))
	print("Enter elements: ")
	a = []
	for i in  range(0,n):
		k = int(input())
		a.append(k)
	return a

# recursive function
def binarysearch_array(a,low,high,search):
    if high >= low:
        mid = (high+low)//2
        a.sort()
        if a[mid]==search: 
            return mid 
        elif a[mid]>search: 
            return binarysearch_array(a,low,mid-1,search) 
        else: 
            return binarysearch_array(a,mid+1,high,search) 
    else: 
        return -1

#function calling 
arr = array_input()
print("Array is: ", arr)
arr.sort()
print("Sorted Array: ",arr)

#search element
x = int(input("Enter search element: "))

result=binarysearch_array(arr,0,len(arr)-1,x)

if result==-1:
    print("element not found")
else:
    print("Element",x,"found at",result,"index")