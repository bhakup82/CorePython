'''
Created on Feb 13, 2014

@author: bkuppuswamy
'''
# simple read operation
f = open('/Users/bkuppuswamy/datascience/firstSteps/outputFromCsv.csv')
print f
for line in f:
    print line.rstrip()
f.close() 

# simple read and write to a file operation
f = open('/Users/bkuppuswamy/datascience/firstSteps/myDataFile.csv','r')
output = open('/Users/bkuppuswamy/datascience/firstSteps/outputFromCsv.csv', 'w')
for line in f:
    output.write(line.rstrip()+'\n')
f.close() 
output.close()



