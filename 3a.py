import time

a = []

def linear_search(a, n, key):
    for i in range(0, n):
        if key == a[i]:
            print("Key element found at position:", i)
            return
    print("Key element not found")


n = int(input("Enter number of elements: "))
for i in range(0, n):
    element = int(input("Enter an element: "))
    a.append(element)

key = int(input("Enter key value: "))

print("An array is:", a)

start = time.time()
print("The key element is:", key)
linear_search(a, n, key)
end = time.time()

print("Time taken to search element using Linear Search:", end - start)

import matplotlib.pyplot as p 
x=list(range(101)) 
y=[i for i in x] 
p.plot(x,y) 
p.title("Linear search - Time Complexity ") 
p.xlabel("Input") 
p.ylabel("Time") 
p.show() 