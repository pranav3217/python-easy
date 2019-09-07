myUniqueList = [] #making list for values
myLeftovers = [] #making list for rejected values
myUniqueList.append(90) #appending an initial value

def Add(a): #function to segregate
  if (a in myUniqueList):
    print ("False")
    myLeftovers.append(a)
  else:
    print ("True")
    myUniqueList.append(a)

Add(80) #test values
Add(90)
Add(60)
Add(80)
print (myUniqueList) #output
print (myLeftovers) #output
