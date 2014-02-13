'''
Created on Feb 13, 2014

@author: bkuppuswamy
'''
def add(a,b):
    return a+b

def addFixedValue(a):
    y=5
    return y+a

print add(1,2)
print addFixedValue(1)
#This is a comment
s="Bharath" # Python provides dynamic typing of variables you donot have to define a type of variable. 
#Python will take care of this for you
x = 1
y =4
z=x+y



i =1 
for i in range(1,10):
    if i<=5:
        print 'Smaller or equal then 5.\n',
    else:
        print 'Larger then 5.\n',
        
sample = "Bharath"

print len(sample) # print length of the string
print sample[0] # get the oth element of sample string
print sample[-1] # gets the last element of teh string
print sample[0:4] # get the first four characters of the string    
print sample[4:] #get elements after 4
print 'B'+'h'+'a'+'r'+'a'
print sample.lower()
print sample.upper()    
print sample.startswith('B')        
print sample.rstrip()

print 'this is a text'+ str(10)
        
           
