#Shifa Mehreen
#121910313005

#Merge Sort (iterative)
  
def merge(le, ri):
    if not len(le) or not len(ri): return le or ri
    result = []
    i, j = 0, 0
    while (len(result) < len(le) + len(ri)):
        if le[i] < ri[j]:
            result.append(le[i])
            i+= 1
        else:
            result.append(ri[j])
            j+= 1
        if i == len(le) or j == len(ri):
            result.extend(le[i:] or ri[j:])
            break
    return result
 
def mergesort(li):
    if len(li) < 2: return li
    mi = int(len(li)/2)
    le = mergesort(li[:mi])
    ri = mergesort(li[mi:])
    return merge(le, ri)

l=list(map(int,input().split()))

print("Sorted array: ",mergesort(l))