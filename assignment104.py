#swapping 2 numbers

#input
a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))

#logic
temp = a #temporary variable 
a = b
b = temp

print("Now 1st number is: ",a)
print("And 2nd number is: ",b)

