import time

a = []

def bubble_sort(a, n):
    for i in range(n):
        for j in range(0, n - 1 - i):
            if a[j] > a[j + 1]:
                temp = a[j]          
                a[j] = a[j + 1]      
                a[j + 1] = temp     
    return a

n = int(input("Enter size: "))
for i in range(n):
    value = int(input("Enter values: "))
    a.append(value)

print("Array before sort:", a)
start = time.time()
bubble_sort(a, n)
end = time.time()
print("Array after sort:", a)
print("Time taken to sort array using bubble sort:", end - start)

x = list(range(0, 101))
y = [i * i for i in x]

import matplotlib.pyplot as p
p.plot(x, y)
p.title("Time Complexity of Bubble Sort")
p.xlabel("Input Size (n)")
p.ylabel("Time / Operations")
p.show()
