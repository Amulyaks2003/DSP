# Class to create a node of linked list
class node:
    def __init__(self, data):
        self.data = data      # stores value
        self.next = None     # stores address of next node


# Class to manage linked list using iterator
class iterator:
    def __init__(self):
        self.head = None     # points to first node (initially empty)


    # Generator function to traverse linked list
    def iterate(self):
        temp = self.head            # start from head
        while temp:                # loop until temp becomes None
            yield temp.data        # return current node data
            temp = temp.next      # move to next node


    # Function to display linked list
    def display(self):
        if self.head is None:      # check if list is empty
            print("List is empty")
            return

        # traverse using iterator and print values
        for item in self.iterate():
            print(item, end="-->")
        print("None")              # end of list

    # Function to insert node at beginning (prepend)
    def prepend(self, newnode):
        newnode.next = self.head  # link new node to old head
        self.head = newnode       # update head to new node

# Creating linked list object
si = iterator()

# Menu driven program
while True:

    print("\n1.PREPEND \t 2.DISPLAY \t 3.EXIT\n")
    choice = int(input("Enter your choice: "))

    # Insert element at beginning
    if choice == 1:
        data = int(input("Enter element:= "))
        si.prepend(node(data))   # create node and add to list

    # Display linked list
    elif choice == 2:
        si.display()

    # Exit program
    elif choice == 3:
        break

    # Invalid input
    else:
        print("Invalid choice")
