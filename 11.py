class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class bst:
    def __init__(self):
        self.root = None

    def insert(self, newnode):
        if self.root is None:
            self.root = newnode
            return
        else:
            temp = self.root
            while True:
                if newnode.data < temp.data:
                    if temp.left is None:
                        temp.left = newnode
                        return
                    else:
                        temp = temp.left
                else:
                    if temp.right is None:
                        temp.right = newnode
                        return
                    else:
                        temp = temp.right

    def search(self, key):
        temp = self.root
        if temp is None:
            return "Tree is empty"

        while True:
            if temp is None:
                return "Element not found"

            if key == temp.data:
                return "Element found"
            elif key < temp.data:
                temp = temp.left
            else:
                temp = temp.right

    def inorder(self, root):
        if root is None:
            return
        self.inorder(root.left)
        print(root.data)
        self.inorder(root.right)


b = bst()

while True:
    choice = int(input("\n1. INSERT \t 2. SEARCH \t 3. DISPLAY \t 4. EXIT\nEnter Your Choice: "))

    if choice == 1:
        item = int(input("Enter an element: "))
        b.insert(node(item))

    elif choice == 2:
        key = int(input("Enter key to search: "))
        print(b.search(key))

    elif choice == 3:
        print("Inorder Traversal:")
        b.inorder(b.root)

    elif choice == 4:
        break

    else:
        print("Invalid choice!")