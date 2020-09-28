#Transpose of sparse matrix

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

#input matrix
x= input_matrix()
print("Given Matrix: ")
display_matrix(x)

#conversion
print("SparseMatrix: ")
x1 = sparseMatrix(x)
display_matrix(x1)

#transpose matrix
def matrixTranspose(a):
    trans= [None]*len(a[0])
    for i in range(len(a)):
        trans[i] = [None]*len(a)
        for j in range(len(a[i])):
            trans[i][j] = a[j][i]

    #print
    print("Transpose Matrix: ")
    display_matrix(trans)

matrixTranspose(x)

#transpose sparse matrix
def trans(a1):
    res = []
    for i in a1:
        res.append([i[1],i[0],i[2]])
    res.sort()

    #print
    print("SparseMatrix Transpose: ")
    display_matrix(res)

trans(x1)




