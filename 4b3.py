import time 
a=[] 
 
def fib(n): 
    if (n==0): 
        return 0 
    if (n==1): 
        return 1 
    else: 
        a[n]=fib(n-1)+fib(n-2) 
        return a[n] 
 
s=time.time()    
n=int(input("enter value for n: ")) 
for i in range(0,n+1): 
       a.insert(i,-1) 
for i in range(n+1): 
    print(fib(i)) 
e=time.time() 
print("time take to find fibonacci series",e-s) 

import matplotlib.pyplot as p 
x=list(range(11)) 
y=[2**i for i in x] 
p.plot(x,y) 
p.title("fibonacci series") 
p.xlabel("input") 
p.ylabel("time taken") 
p.show() 