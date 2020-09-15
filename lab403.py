#Shifa Mehreen
#121910313005

#Matrix to SparseMatrix using functions
#and taking input from user

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
    
#threshold value

    l = int(input("Enter threshold value: "))

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] <l+1:
                matrix[i][j] = 0

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



#input matrix
x= input_matrix()
print("Given Matrix: ")
display_matrix(x)

#conversion
sparseMatrix(x)
