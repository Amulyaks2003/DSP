class student:
    def __init__(self):
        self.rollno = input("Enter Roll Number : ")
        self.name = input("Enter Name : ")
        self.python = int(input("Enter Python Marks : "))
        self.java = int(input("Enter JAVA Marks : "))
        self.os = int(input("Enter OS Marks : "))
        self.se = int(input("Enter SE Marks : "))

    def display(self):
        print("\nStdeunt name is:", self.name)
        print("Stdeunt Roll_NO is:", self.rollno)
        print("Python marks is:", self.python)
        print("java marks is:", self.java)
        print("OS marks is:", self.os)
        print("SE marks is:", self.se)

    def total_avg(self):
        total = self.python + self.java + self.os + self.se
        avg = total / 4
        print("Total marks is:", total)
        print("avg marks is:", avg)

    def result(self):
        if (self.python < 35):
            print("failed in python")
        else:
            print("pass in python")
        if (self.java < 35):
            print("failed in java")
        else:
            print("pass in java")
        if (self.os < 35):
            print("failed in os")
        else:
            print("pass in java")
        if (self.se < 35):
            print("failed in se")
        else:
            print("pass in se")


n = int(input("Enter number of students: "))
students = []

for i in range(n):
    print("\nEnter details of student", i + 1)
    students.append(student())

for s in students:
    s.display()
    s.total_avg()
    s.result()

import matplotlib.pyplot as p

x = list(range(101))
y = [i for i in x]

p.plot(x, y)
p.title("ADT - Time Complexity")
p.xlabel("Input")
p.ylabel("Time")
p.show()