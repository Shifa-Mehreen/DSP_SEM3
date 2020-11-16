#Shifa Mehreen
#121910313005

#Postfix to Infix

exp=input("Enter ur postfix expression: ")

def postfix(exp):
  stack = []
  
  for i in exp:
    if i not in "*/+-":
      stack.append(i)
    else:
      op1 = stack.pop()
      op2 = stack.pop()
      stack.append(op2+i+op1)

  print(''.join(stack))

postfix(exp)

