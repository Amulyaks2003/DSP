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
                if newnode.data <= temp.data:                     
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
         
    def preorder(self, root):         
        if root is None:               
            return 
        print(root.data, end=" ") 
        self.preorder(root.left)         
        self.preorder(root.right) 

    def inorder(self, root):         
        if root is None:               
            return  
        self.inorder(root.left) 
        print(root.data, end=" ") 
        self.inorder(root.right) 

    def postorder(self, root):         
        if root is None:               
            return  
        self.postorder(root.left)         
        self.postorder(root.right) 
        print(root.data, end=" ") 


# Main Program
b = bst()

while True: 
    choice = int(input(
        "\n1. INSERT\n2. DFS PREORDER\n3. DFS INORDER\n4. DFS POSTORDER\n5. EXIT\nEnter your choice: "
    ))

    if choice == 1: 
        item = int(input("Enter element to insert into Tree: ")) 
        b.insert(node(item)) 
        
    elif choice == 2: 
        print("Preorder traversal is: ", end="") 
        b.preorder(b.root) 
        print()
         
    elif choice == 3: 
        print("Inorder traversal is: ", end="") 
        b.inorder(b.root) 
        print()
         
    elif choice == 4: 
        print("Postorder traversal is: ", end="") 
        b.postorder(b.root) 
        print()

    elif choice == 5:
        print("Exiting...")
        break
        
    else: 
        print("Invalid choice!")