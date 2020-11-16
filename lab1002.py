#Shifa Mehreen
#121910313005

#Infix to Postfix

infix=input()
s=[]
prec={"+":1,"-":1,"*":2,"/":2,"^":3}
postfix=""
def not_greater(h):
  try:
    g=prec[h]
    f=prec[s[-1]]
    if g<=f:
      return True
    else:
      return False
  except:
    return False
for i in infix:
  if i=="(":
    s.append(i)
  elif i.isalpha():
    postfix+=i
  elif i==")":
    while s[-1]!="(" and len(s)>0:
      postfix+=s.pop()
    s.pop()
  else:
    while len(s)>0 and not_greater(i):
      postfix+=s.pop()
    s.append(i)
while len(s)>0:
  postfix+=s.pop()
print(postfix)