'''
Created on Feb 13, 2014

@author: bkuppuswamy
'''
myList = ["Linux","Mac OS", "Windows"]
#print the first line element
print myList[0]
#Print last element
print myList[-1]
#sublist first,secodn and third element
print myList[0:2]
#Add elements to thelist
myList.append("Android")
#print the content using for loop
for element in myList:
    print element
    
#If you want to remove duplicates in a list use set()
myList.append("Android")
print myList
print list(set(myList))    