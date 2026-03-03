import time 
a=[] 
 
def divide(a,low,high): 
    if(low<high): 
        mid=(low+high)//2 
        divide(a,low,mid) 
        divide(a,mid+1,high) 
        merge(a,low,mid,high) 
 
def merge(a,low,mid,high): 
          temp=[] #temporary array to store merged result
          i=low #pointer for left subarray
          k=low #index for inserting into temp
          j=mid+1 #pointer for right subarray
          while(i<=mid and j<=high): #Runs while both subarrays still have elements.
                if(a[i]<a[j]): #Compare left and right elements.
                    temp.insert(k,a[i])  # Insert left element
                    i=i+1  # Move left pointer
                    k=k+1  # Move temp pointer
                else: 
                    temp.insert(k,a[j])   # Insert right element
                    j=j+1  # Move right pointer
                    k=k+1  # Move temp pointer
          while(i<=mid):  # Copy remaining elements from left subarray (if any)
                temp.insert(k,a[i]) 
                k=k+1 
                i=i+1 
          while(j<=high):  # Copy remaining elements from right subarray (if any)
                temp.insert(k,a[j]) 
                k=k+1 
                j=j+1 
          p=low   # Pointer for original array
          m=0    # Pointer for temp array
          while(p<k): # Copy merged elements back into original array
                     a[p]=temp[m] 
                     p=p+1 
                     m=m+1 
 
n=int(input("Enter size:")) 
for i in range(0,n): 
    v=int(input("Enter values:")) 
    a.append(v) 
start=time.time() 
print("the array before sort:",a) 
divide(a,0,n-1) 
end=time.time() 
print("the array after sort:",a) 
print("time taken to sort an array using Merge sort",end-start)

import math 
import matplotlib.pyplot as p 
p.title("Merge Sort ") 
p.xlabel("Input") 
p.ylabel("Time") 
x=list(range(1,101)) 
y=[i*math.log(i) for i in x] 
p.plot(x,y) 
p.show() 