#Shifa Mehreen
#121910313005

#Insertion Sort (iterative)

a=list(map(int,input().split()))

for i in range(1,len(a)):
  k=a[i] #key: 2nd element
  j=i-1 

  while j>=0 and a[j]>k: #checking
    a[j+1]=a[j] #pushing elements to right
    j-=1
  a[j+1]=k #placing key into array

print("Sorted Array: ",a)