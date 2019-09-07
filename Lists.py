myUniqueList = []
myLeftovers = []
myUniqueList.append(90)
def Add(a):
  if (a in myUniqueList):
    print ("False")
    myLeftovers.append(a)
  else:
    print ("True")
    myUniqueList.append(a)
Add(80)
Add(90)
Add(60)
Add(80)
print (myUniqueList)
print (myLeftovers)
