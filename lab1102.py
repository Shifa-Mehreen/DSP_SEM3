#Shifa Mehreen
#121910313005

#Implement the parenthesis matching algorithm using stack

def Parentheseschecker(s):
  stack=[]
  o="{[("
  c="}])"
  for i in s:
    if i in o:
      stack.append(i)
    else:
      if len(stack)==0:
        return False
      else:
        if c.index(i)==o.index(stack[-1]):
          stack.pop()
    print(*stack)
  if len(stack)==0:
    return True
  return False
  
s=input("Enter a string of braces: ")
t=Parentheseschecker(s)
print(t)
		
