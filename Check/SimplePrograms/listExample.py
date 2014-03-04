print [1,3,True,6.5]
myList = [1,3,True,6.5]
print myList
# Lists are considered sequentially ordered 
myList1 = [0]*6
print myList1
myList2 = [1,2,3,4]
A = [myList2]*3
print A
myList2[2]=45
A = [myList2]*3
print A
mlist = [1024,3,4.5,True,6.5]
mlist.append(False)
print mlist
print mlist.pop()
print mlist.pop(1)
print mlist
mlist.pop(2)
print mlist
mlist.sort(cmp=None, key=None, reverse=False)
mlist.reverse()
mlist.count(6.5)
mlist.index(4.5)
mlist.remove(6.5)
del mlist[0]
print mlist