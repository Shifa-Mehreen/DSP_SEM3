#Shifa Mehreen
#121910313005

#Selection Sort (recursive)


def selectionsort(ar,i,n):
    min_i=i
    for j in range(i+1,n):
        if ar[j]<ar[min_i]:
            min_i=j
    ar[i],ar[min_i]=ar[min_i],ar[i]
    if i+1<n:
        selectionsort(ar,i+1,n)

ar=list(map(int,input().split()))

selectionsort(ar,0,len(ar))
print("Sorted Array:" ,ar)