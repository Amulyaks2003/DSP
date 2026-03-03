import time 
a=[] 
def binary_search(a,low,high,key): 
    if(low<=high): 
        mid=(low+high)//2 
        if key is a[mid]: 
            print("key element found at position:",mid) 
            return 
        elif key<a[mid]: 
            return binary_search(a,low,mid-1,key) 
        else: 
            return binary_search(a,mid+1,high,key)       
    print("key element not found") 
 
n=int(input("enter number of elements:")) 
for i in  range(0,n): 
    element=int(input("enter element:")) 
    a.append(element) 
key=int(input("enter key value:")) 
start=time.time() 
print("the array is:",a) 
print("the key element is:",key) 
result=binary_search(a,0,n-1,key) 
end=time.time() 
print("Time taken to Search an element using Binary search :" ,end-start) 

import math 
import matplotlib.pyplot as p 
 
x=list(range(1,101)) 
y=[math.log(i) for i in x] 
p.plot(x,y) 
p.title("Binary search Time Complexity") 
p.xlabel("Input") 
p.ylabel("Time") 
p.show()