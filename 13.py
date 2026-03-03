class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    # Hash Function
    def hash_function(self, key):
        return key % self.size

    # Insert using Linear Probing
    def insert(self, key):
        index = self.hash_function(key)

        if self.table[index] is None:
            self.table[index] = key
        else:
            print("Collision occurred at index", index)
            original_index = index
            index = (index + 1) % self.size

            while index != original_index:
                if self.table[index] is None:
                    self.table[index] = key
                    return
                index = (index + 1) % self.size

            print("Hash Table is Full")

    # Display Hash Table
    def display(self):
        print("\nHash Table:")
        for i in range(self.size):
            print("Index", i, ":", self.table[i])


# Main Program
size = int(input("Enter size of Hash Table: "))
h = HashTable(size)

while True:
    print("\n1. Insert\n2. Display\n3. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        key = int(input("Enter key to insert: "))
        h.insert(key)

    elif choice == 2:
        h.display()

    elif choice == 3:
        break

    else:
        print("Invalid choice!")