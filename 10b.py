class que:
    def __init__(self):
        self.queue = []

    def isempty(self):
        return len(self.queue) == 0

    def length(self):
        print("Number of elements in the queue:", len(self.queue))

    def enqueue(self, item):
        self.queue.append(item)
        print("Element inserted successfully.")

    def dequeue(self):
        if self.isempty():
            print("Queue is empty")
        else:
            priority = 0
            for i in range(len(self.queue)):
                if self.queue[i] < self.queue[priority]:
                    priority = i
            print("Dequeued element is:", self.queue.pop(priority))

    def display(self):
        if self.isempty():
            print("Queue is empty")
        else:
            print("Queue elements are:", self.queue)


q = que()

while True:
    choice = int(input("\n1.ENQUEUE \t 2.DEQUEUE \t 3.LENGTH \t 4.EMPTY \t 5.DISPLAY \t 6.EXIT\nEnter your choice: "))

    if choice == 1:
        element = int(input("Enter element to enqueue into queue: "))
        q.enqueue(element)

    elif choice == 2:
        q.dequeue()

    elif choice == 3:
        q.length()

    elif choice == 4:
        print("Queue is empty:", q.isempty())

    elif choice == 5:
        q.display()

    elif choice == 6:
        break

    else:
        print("Invalid choice!")