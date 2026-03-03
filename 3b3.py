import time

a = []
def insertion_sort(a, n):
    for i in range(1, n):
        k = a[i]         
        j = i - 1         

        while j >= 0 and a[j] > k:
            a[j + 1] = a[j]
            j = j - 1

        a[j + 1] = k      


n = int(input("Enter size: "))
for i in range(n):
    value = (int(input("Enter values: ")))
    a.append(value)

print("The array before sort:", a)
start = time.time()
insertion_sort(a, n)
end = time.time()
print("The array after sort:", a)
print("Time taken to sort an array using insertion sort:", end - start)

import matplotlib.pyplot as p 
x=list(range(1,101)) 
y=[i*i for i in x] 
p.plot(x,y) 
p.title("Time complexity of Insertion Sort") 
p.xlabel("Input") 
p.ylabel("Time") 
p.show()