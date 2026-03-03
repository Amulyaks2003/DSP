import time

a = []

def selection_sort(a, n):
    for i in range(0, n - 1):
        min = i
        for j in range(i + 1, n):
            if a[j] < a[min]:
                min = j
        # swap A[i] and A[min] using temp
        temp = a[i]
        a[i] = a[min]
        a[min] = temp

    return a

n = int(input("Enter size: "))
for i in range(n):
    value = int(input("Enter values: "))
    a.append(value)

print("The array before sort:", a)
start = time.time()
selection_sort(a, n)
end = time.time()
print("The array after sort:", a)
print("Time taken to sort an array using selection sort:", end - start)

x = list(range(0, 101))
y = [i * i for i in x]

import matplotlib.pyplot as p
p.plot(x, y)
p.title("Time Complexity of Selection Sort")
p.xlabel("Input Size (n)")
p.ylabel("Time / Operations")
p.show()
