class myclass:
   i = 0
   j = 1

   def __init__(self):
      print("parent")

cc=myclass()

print(cc.i)

class derievedclass(myclass):
     k=2
     def __init__(self):
         print("child")

  
dd = derievedclass();

print(dd.j)


print(dd.k)
 
   
