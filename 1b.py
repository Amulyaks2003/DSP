class student:
    def __init__(self):
        self.rollno = input("Enter Roll Number : ")
        self.name = input("Enter Name : ")
        self.python = int(input("Enter Python Marks : "))
        self.java = int(input("Enter JAVA Marks : "))
        self.os = int(input("Enter OS Marks : "))
        self.se = int(input("Enter SE Marks : "))

    def display(self):
        print("\nStudent name is:", self.name)
        print("Student Roll_NO is:", self.rollno)
        print("Python marks is:", self.python)
        print("JAVA marks is:", self.java)
        print("OS marks is:", self.os)
        print("SE marks is:", self.se)

    def total_avg(self):
        total = self.python + self.java + self.os + self.se
        avg = total / 4
        print("Total marks is:", total)
        print("Average marks is:", avg)

    def result(self):
        if self.python < 35:
            print("Failed in Python")
        else:
            print("Pass in Python")

        if self.java < 35:
            print("Failed in Java")
        else:
            print("Pass in Java")

        if self.os < 35:
            print("Failed in OS")
        else:
            print("Pass in OS")

        if self.se < 35:
            print("Failed in SE")
        else:
            print("Pass in SE")


# Main Program
n = int(input("Enter number of students: "))
students = []

for i in range(n):
    print("\nEnter details of student", i + 1)
    students.append(student())

for s in students:
    s.display()
    s.total_avg()
    s.result()

