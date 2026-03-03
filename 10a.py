class Queue:
    # Constructor - Initializes an empty list to represent the queue
    def __init__(self):
        self.queue = []   # List to store queue elements

    # Method to check whether queue is empty
    def isempty(self):
        return len(self.queue) == 0

    # Method to display length of queue
    def length(self):
        print("Number of elements in the queue:", len(self.queue))

    # Method to insert element at rear (Enqueue operation)
    def enqueue(self, item):
        self.queue.append(item)   # Adds element at the end
        print("Contents of the queue:", self.queue)

    # Method to remove element from front (Dequeue operation)
    def dequeue(self):
        if len(self.queue) == 0:
            print("Queue is empty")
        else:
            print("Dequeued element is:", self.queue.pop(0))  # Removes first element
            print("Contents of the queue:", self.queue)


# Creating Queue object
q = Queue()

# Menu-driven program
while True:
    choice = int(input("\n1.ENQUEUE \t 2.DEQUEUE \t 3.LENGTH \t 4.EMPTY \t 5.EXIT\nEnter your choice: "))

    if choice == 1:   # Corrected (use == instead of is)
        element = int(input("Enter element to enqueue into queue: "))
        q.enqueue(element)

    elif choice == 2:
        q.dequeue()

    elif choice == 3:
        q.length()

    elif choice == 4:
        print("Queue is empty:", q.isempty())

    elif choice == 5:
        print("Exiting program...")
        break

    else:
        print("Invalid choice!")