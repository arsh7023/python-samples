import sys
def fib():
    #print ("start")
    #print (sys.argv[0])

    a,b = 0,1
    while a < 10:
        print(a, end=',')
        a,b = b, a+b

fib()