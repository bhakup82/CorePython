myTuple = (2,True,4.96)
print myTuple
print len(myTuple)
print myTuple[0]
print myTuple*3
print myTuple[0:2]

mySet = {3,6,"cat",4.5,False}
print mySet
print len(mySet)
print 3 in mySet
print 'b' in mySet
mySet = {False,4.5,3,6,'cat'}
print mySet
yourSet = {99,3,100}
print mySet.union(yourSet)
print mySet | yourSet
print mySet.intersection(yourSet)
print mySet & yourSet
print mySet.difference(yourSet)
print mySet-yourSet
print {3,100}.issubset(yourSet)
print {3,100}<=yourSet
print mySet.add("house")