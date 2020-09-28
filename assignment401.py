#Shifa Mehreen
#121910313005

#Addition of sparse matrix

#input 
def input_matrix():
    #size of matrix 
    r= int(input("Enter the number of rows: ")) 
    c = int(input("Enter the number of columns: ")) 
      
    matrix = []

    #taking in elements
    print("Enter elements: ") 
     
    for i in range(r):          
        a =[] 
        for j in range(c):
            k = int(input())
            a.append(k)
        matrix.append(a)
    return matrix

#printing elements
def display_matrix(matrix):
    for i in matrix:
        for j in i:
            print(j, end=" ")
        print()

#SparseMatrix
def sparseMatrix(matrix):

    sparsematrix = [] #declare empty list

    #looping
    #and checking for non-zero elements
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] != 0:

                temp=[] #temporary list

                temp.append(i) #adding row index
                temp.append(j) # adding column index
                temp.append(matrix[i][j]) #value of tht non-zero element

                #appending temp to sparsematrix
                sparsematrix.append(temp)

    return sparsematrix

#input matrix1
x= input_matrix()
print("Given Matrix 1: ")
display_matrix(x)

#conversion1
print("SparseMatrix 1: ")
x1 = sparseMatrix(x)
display_matrix(x1)

#input matrix2
y= input_matrix()
print("Given Matrix 2: ")
display_matrix(y)

#conversion2
print("SparseMatrix 2: ")
y1 = sparseMatrix(y)
display_matrix(y1)

#addition of given matrix
def add_matrices(a,b):
    #add
    if len(a) != len(b):
        print("Addition not possible! Enter matrices with same lengths!!")

    else:
        sum = []
    
        for i in range(len(a)):
            tempo = []
            for j in range(len(a)):

                tempo.append(a[i][j] + b[i][j])
            sum.append(tempo)

 
        #print
        print("Addition of matrix 1 and 2: ")
        display_matrix(sum)
        
add_matrices(x,y)

#addition of sparse matrices
def sparse_add(a1,b1):
    r = [] 
    l1 = len(a1)
    l2 = len(b1)
    if l1==0 : r = b1
    if l2==0 : r = a1
    i = 0
    j = 0
    while l1>0 and l2>0:
        if a1[i][0]==b1[j][0] and a1[i][1]==b1[j][1]:
            r.append([a1[i][0],a1[i][1],a1[i][2]+b1[j][2]])
            i += 1
            j += 1
        else:
            m = min(a1[i],b1[j])
            r.append(m)
            if m==a1[i]:
                i += 1
            else:
                j += 1
        if i>=l1:
            for x in range(j,l2):
                r.append(b1[x])
            break
        if j>=l2:
            for x in range(i,l1):
                r.append(a1[x])
            break
    #print
    print("Sparse Matrix Addition of matrix 1 and 2: ")
    display_matrix(r)

sparse_add(x1,y1)







