'''
f = open("while1.py", "r")
#print (f.readline())
i=0
for line in f:
   print(str(i+1) + ":::")
   i+=1
   print(line)

f.close()
'''

# file handle fh
fh = open('while1.py')
while True:
    # read line
    line = fh.readline()
    # in python 2, print line
    # in python 3
    print(line)
    # check if line is not empty
    if not line:
        break
fh.close()	
