print("Python program to Use and demonstrate basic data structures\n")
name=input("Enter name:")
python=int(input("Enter python marks:"))
os=int(input("Enter os marks:"))
java=int(input("Enter java marks:"))
se=int(input("Enter se marks:"))
total=python+os+java+se
avg=total/4
print("\nStudent name is:", name,"Data type is:",type(name))
print("python marks is:", python,"Data type is:",type(python))
print("os marks is:", os,"Data type is:",type(os))
print("java marks is:", java,"Data type is:",type(java))
print("se marks is:", se,"Data type is:",type(se))
print("\ntotal marks is:", total,"Data type is:",type(total))
print("\nAverage is:", avg,"Data type is:",type(avg))
if avg>90:
 a=True
else:
 a=False
 print("\nAverage is gretaer than 90 ?", a, "Data type is:", type(a))
 print("\nList is a collection which is ordered and changeable. Allows duplicate members")
 example = ["AIEMS", "cse", "4"]
 print(example, "Data type is:", type(example))
 print("\nTuple is a collection which is ordered and unchangeable. Allows duplicate members.")
 example = ("AIEMS", "cse", "4", "cse")
 print(example, "Data type is:", type(example))
 print("\nSet is a collection which is unordered, unchangeable, and unindexed. No duplicate members")
 example = {"AIEMS", "cse", "4"}
 print(example, "Data type is:", type(example))
 print("\nDictionary is a collection which is ordered and changeable. No duplicate members")
 example = {"College": "AIEMS", "branch": "cse", "sem": "4"}
 print(example, "Data type is:", type(example))

