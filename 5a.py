class node: # creating node
    def __init__(self, data):
        self.data = data # stores the value 
        self.next = None # stores address of next node (initially None)


class singlylinkedlist:
    def __init__(self):
        self.head = None # head points to first node, initialy list is empty so head = none

    # insert at beginning
    def prepend(self, newnode): 
        newnode.next = self.head 
        self.head = newnode #head moves to new node

    # delete from beginning
    def remove(self): # if list empty -> print message
        if self.head is None:
            print("List is empty")
        else: # otherwise move head to second node
            self.head = self.head.next

    # display list
    def display(self):
        temp = self.head # start from head
        while temp is not None:
            print(temp.data, end="-->")
            temp = temp.next # print data move to next node, continue till none
        print("None")

    # search element
    def search(self, key): #Traverse list comparing each node’s data with key
        temp = self.head
        while temp is not None and temp.data != key:
            temp = temp.next

        if temp is None:
            print("Key not found")
        else:
            print("Key found")


# main program
s = singlylinkedlist() #Create list object
#Take number of nodes
n = int(input("Enter number of nodes: "))

#Insert nodes
for i in range(n):
    val = int(input("Enter value: "))
    s.prepend(node(val))

#Display list
print("\nLinked List:")
s.display()

key = int(input("\nEnter element to search: "))
s.search(key)

d = int(input("\nHow many nodes to delete from beginning: "))
for i in range(d):
    s.remove()

print("\nList after deletion:")
s.display()
