#Shifa Mehreen
#121910313005

#Merge Sort (recursive)

def mergesort(ar):
  if len(ar)>1:
    mid=len(ar)//2
    left=ar[:mid]
    right=ar[mid:]

    mergesort(left)
    mergesort(right)

    i=0
    j=0
    k=0

    while i<len(left) and j<len(right):
      if left[i]<=right[j]:
        ar[k]=left[i]
        i+=1
        k+=1
      else:
        ar[k]=right[j]
        j+=1
        k+=1

    while i<len(left):
      ar[k]=left[i]
      i+=1
      k+=1
    while j<len(right):
      ar[k]=right[j]
      j+=1
      k+=1


ar=list(map(int,input().split()))

mergesort(ar)
print("Sorted array:" ,ar)