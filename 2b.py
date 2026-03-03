rollno = []
name = []
python = []
java = []
os = []
se = []
n = int(input("enter number of students"))
for i in range(n):
    rollno.append(input("Enter Roll Number : "))
    name.append(input("Enter Name : "))
    python.append(int(input("Enter Python Marks : ")))
    java.append(int(input("Enter JAVA Marks : ")))
    os.append(int(input("Enter OS Marks : ")))
    se.append(int(input("Enter SE Marks : ")))

for i in range(n):
    print("\n Stdeunt name is:", name[i])
    print("Stdeunt Roll_NO is:", rollno[i])
    print("Python marks is:", python[i])
    print("java marks is:", java[i])
    print("OS marks is:", os[i])
    print("SE marks is:", se[i])

    total = python[i] + java[i] + os[i] + se[i]
    avg = total / 4
    print("Total marks is:", total)
    print("avg marks is:", avg)

    if (python[i] < 35):
        print("failed in python")
    else:
        print("pass in python")
    if (java[i] < 35):
        print("failed in java")
    else:
        print("pass in java")
    if (os[i] < 35):
        print("failed in os")
    else:
        print("pass in java")
    if (se[i] < 35):
        print("failed in se")
    else:
        print("pass in se")

import matplotlib.pyplot as p
x=list(range(101))
y=[i for i in x]
p.plot(x,y)
p.title("Array - Time Complexity ")
p.xlabel("Input")
p.ylabel("Time")
p.show()