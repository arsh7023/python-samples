import mymodule

mymodule.hello()

print ("hello ali")

i=2

print(i)

"""
for x in range(3):
 if(x==2):
  print(x)
 elif (x==1):
  print(1000)
 else:
  print(x+10)#
"""

#for x in range(1,10,4):
#   print(x)

str1="alireza shamakhy"

print (str1[0])
print(len(str1))
print(str1[0:1])

print(str1[0:len(str1)])

def func1(a,b):
   print("sum is:"+ str(a+b))

func1(10,2)


class Myclass:
  x=5
  def __init__(self,name):
    print("condtructor:"+ name)

  def cfunc1(self):
    print("inside class function")

cc=Myclass("reza")
cc.cfunc1()
print(cc.x) 
