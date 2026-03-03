# Node class represents each individual element in the list
class Node:
    def __init__(self, data):
        self.data = data        # Stores value of node
        self.next = None        # Pointer to next node
        self.prev = None        # Pointer to previous node


# Circular Doubly Linked List class
class CircularDoublyLinkedList:
    def __init__(self):
        self.head = None       # Points to first node
        self.tail = None       # Points to last node

    # Display all nodes in circular manner
    def display(self):

        # If list is empty
        if self.head is None:
            print("Linked list is empty")
            return

        temp = self.head      # Start traversal from head

        # Infinite loop because list is circular
        while True:
            print(temp.data, end=" <-> ")  # Print current node data
            temp = temp.next              # Move to next node

            # Stop when we reach head again
            if temp == self.head:
                break

        print()               # New line after displaying list

    # Insert new node at the end of the circular doubly linked list
    def append(self, newnode):

        # If list is empty (first node insertion)
        if self.head is None:
            self.head = newnode
            self.tail = newnode

            # First node points to itself (circular)
            newnode.next = newnode
            newnode.prev = newnode

        # If list already contains nodes
        else:
            newnode.prev = self.tail     # New node points back to old tail
            newnode.next = self.head    # New node points forward to head

            self.tail.next = newnode    # Old tail points to new node
            self.head.prev = newnode    # Head points back to new node

            self.tail = newnode         # Update tail to new node

    # Delete node by value
    def remove(self, key):

        # If list is empty
        if self.head is None:
            print("Linked list is empty")
            return

        temp = self.head   # Start searching from head

        # Infinite loop because circular list has no NULL
        while True:

            # If key is found
            if temp.data == key:

                # Case 1: Only one node in list
                if self.head == self.tail:
                    self.head = None
                    self.tail = None

                # Case 2: Deleting head node
                elif temp == self.head:
                    self.head = temp.next        # Move head forward
                    self.head.prev = self.tail  # Update backward link
                    self.tail.next = self.head  # Update forward link

                # Case 3: Deleting tail node
                elif temp == self.tail:
                    self.tail = temp.prev       # Move tail backward
                    self.tail.next = self.head
                    self.head.prev = self.tail

                # Case 4: Deleting middle node
                else:
                    temp.prev.next = temp.next  # Previous node skips current
                    temp.next.prev = temp.prev  # Next node skips current

                print("Node deleted")
                return

            temp = temp.next   # Move to next node

            # If we returned to head, key not present
            if temp == self.head:
                print("Key not found")
                return


# Create Circular Doubly Linked List object
cdll = CircularDoublyLinkedList()

# Menu driven infinite loop
while True:
    print("\n1.APPEND \t 2.DISPLAY \t 3.DELETE \t 4.EXIT")

    choice = int(input("Enter your choice: "))

    # Insert element
    if choice == 1:
        data = int(input("Enter element to insert: "))
        cdll.append(Node(data))   # Create node and append

    # Display list
    elif choice == 2:
        cdll.display()

    # Delete element
    elif choice == 3:
        key = int(input("Enter key to delete: "))
        cdll.remove(key)

    # Exit program
    elif choice == 4:
        break

    # Invalid input
    else:
        print("Invalid choice")
