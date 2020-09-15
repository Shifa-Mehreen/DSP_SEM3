#Shifa Mehreen
#121910313005

#Matrix to SparseMatrix using functions

#function to print a matrix
def display_matrix(matrix):
    for i in matrix:
        for j in i:
            print(j, end=" ")
        print()

#matrix initialization
a   = ([0,0,0,1],
       [1,0,0,2],
       [3,0,0,0],
       [0,4,0,2])

#print given matrix
print("Given Matrix:")
display_matrix(a)


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

    #display sparsematrix
    print("\nSparseMatrix:")
    display_matrix(sparsematrix)


#conversion
sparseMatrix(a) #using function






