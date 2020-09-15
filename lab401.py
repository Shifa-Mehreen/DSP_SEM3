#Shifa Mehreen
#121910313005

#represent a sparse matrix

#matrix initialization
matrix = ([0,0,0,1],
	      [1,0,0,2],
	      [3,0,0,0],
	      [0,4,0,2])

#printing initialized matrix
print("Given Matrix: ")
for i in matrix:
	for j in i:
		print(j, end=" ")
	print()

#SparseMatrix

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

			sparsematrix.append(temp) #appending temp to sparsematrix

#printing SparseMatrix
print("\nSparseMatrix: ")
for i in sparsematrix:
	for j in i:
		print(j, end =" ")
	print()


