# Node class represents each element of the doubly linked list
class Node:
    def __init__(self, data):
        self.data = data        # Stores value of the node
        self.next = None        # Pointer to next node
        self.prev = None        # Pointer to previous node


# DoublyLinkedList class manages all operations
class DoublyLinkedList:
    def __init__(self):
        self.head = None        # Points to first node
        self.tail = None        # Points to last node

    # Display all nodes from head to tail
    def display(self):
        # Check if list is empty
        if self.head is None:
            print("Linked list is empty")
            return

        temp = self.head       # Start from first node

        # Traverse until last node
        while temp:
            print(temp.data, end=" <-> ")   # Print current node data
            temp = temp.next               # Move to next node

        print("None")          # Indicates end of list

    # Search for a value in the list
    def search(self, key):
        temp = self.head      # Start searching from head

        # Move forward until key is found or list ends
        while temp and temp.data != key:
            temp = temp.next # Move to next node

        # If temp is not None, key is found
        if temp:
            print("Key found")
        else:
            print("Key not found")

    # Insert a new node at the end
    def append(self, newnode):

        # If list is empty, new node becomes head and tail
        if self.head is None:
            self.head = newnode
            self.tail = newnode

        # If list already contains nodes
        else:
            self.tail.next = newnode   # Old tail points to new node
            newnode.prev = self.tail  # New node points back to old tail
            self.tail = newnode       # Update tail to new node

    # Delete node by value
    def remove(self, key):
        temp = self.head       # Start from head

        # If list is empty
        if temp is None:
            print("Linked list is empty")
            return

        # Search for the node to delete
        while temp and temp.data != key:
            temp = temp.next

        # If key not found
        if temp is None:
            print("Key not found")
            return

        # Case 1: Deleting first node (head)
        if temp == self.head:
            self.head = temp.next       # Move head forward
            if self.head:
                self.head.prev = None  # Remove backward link
            else:
                self.tail = None       # List became empty

        # Case 2: Deleting last node (tail)
        elif temp == self.tail:
            self.tail = temp.prev      # Move tail backward
            self.tail.next = None

        # Case 3: Deleting middle node
        else:
            temp.prev.next = temp.next   # Previous node points to next
            temp.next.prev = temp.prev   # Next node points to previous

        print("Node deleted successfully")


# Create DoublyLinkedList object
dll = DoublyLinkedList()

# Infinite loop for menu driven program
while True:
    print("\n1.APPEND  2.DISPLAY  3.SEARCH  4.DELETE  5.EXIT")
    choice = int(input("Enter your choice: "))

    # Insert element
    if choice == 1:
        data = int(input("Enter element to insert: "))
        dll.append(Node(data))    # Create new node and append

    # Display list
    elif choice == 2:
        dll.display()

    # Search element
    elif choice == 3:
        key = int(input("Enter key to search: "))
        dll.search(key)

    # Delete element
    elif choice == 4:
        key = int(input("Enter key to delete: "))
        dll.remove(key)

    # Exit program
    elif choice == 5:
        print("Program terminated")
        break

    # Invalid input
    else:
        print("Invalid choice")
