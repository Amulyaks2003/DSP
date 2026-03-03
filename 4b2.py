import time 
 
a=[] 
 
def qs(a,low,high): 
    if(low<high): 
        pivot=divide(a,low,high) 
        qs(a,low,pivot-1) # Sort left subarray
        qs(a,pivot+1,high) # Sort right subarra
         
def divide(a,low,high): 
         pivot=a[low] #First element is chosen as pivot.
         i=low+1 #i moves from left to right
         j=high #j moves from right to left
         while 1: #Runs until pivot is placed correctly.
            while(i<high)and(pivot>=a[i]): 
                  i=i+1 #Skips elements smaller than pivot.
            while(pivot<a[j]): 
                    j=j-1 #Skips elements larger than pivot.
            if i<j: 
                  a[i],a[j]=a[j],a[i] #Swaps wrong-positioned elements.
            else: 
                a[low],a[j]=a[j],a[low] #Else: Place pivot
                return j 
 
n=int(input("Enter size:")) 
for i in range(0,n): 
    value=int(input("Enter values:")) 
    a.append(value) 
start=time.time() 
print("the array before sort:",a) 
qs(a,0,n-1) 
end=time.time() 
print("the array after sort:",a) 
print("time taken to sort an array using Quick sort",end-start) 

import math 
import matplotlib.pyplot as p 
p.title("Quick Sort ") 
p.xlabel("Input") 
p.ylabel("Time") 
x=list(range(1,101)) 
y=[i*math.log(i) for i in x] 
p.plot(x,y) 
p.show()