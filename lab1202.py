#Selection Sort
#121910313005

#Selection Sort (iterative)

a = list(map(int,input().split()))
  
for i in range(len(a)): 
    min_num = i  #take min as 1st element

    for j in range(i+1, len(a)): #transvering till end of the loop
        if a[min_num] > a[j]: #checking for min num
            min_num = j #index assignment   

    a[i], a[min_num] = a[min_num], a[i] #swap

#printing  
print ("Sorted array: ", a)  