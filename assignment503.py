#Shifa Mehreen
#121910313005

#Binary search with  test cases

#function
def binarysearch_array(a,x):
    print("Array is: ",a)
    a.sort() 
    print("Sorted array is: ",a)

    #taking ranges
    f = 0
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



#test cases

#1
print("TestCase1: ")
a1 = [1,2,4,6,8,10,12,14,16,20] #sorted list
x1 = 2       
#function calling
binarysearch_array(a1,x1)

#2
print("TestCase2: ")
a2 = [2,5,25,11,6,8,19,55,15] #unsorted list
x2 = 8      
#function calling
binarysearch_array(a2,x2)

#3
print("TestCase3: ")
a3 = [3,6,7,5,7,9,10,4,2,13,16,3,2,9,5] #repeated elements list
x3 =  5   
#function calling
binarysearch_array(a3,x3)

#4
print("TestCase4: ")
a3 = [2,5,7,9,10,11,6,9,3,1,2,88] #list
x3 = 4    #element that's not present in the list
#function calling
binarysearch_array(a3,x3)