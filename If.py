def check(a,b,c):
  a = int(a)
  b=  int(b)
  c=  int(c)
  if a==b or b==c or a==c:
    print ("True")
  else:
    print ("False")

check (5,7,5) #Two of the values are equal case
check (5,7,"5") #String input case
check (5,6,7) #Unequal values case
