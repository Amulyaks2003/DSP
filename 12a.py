from collections import deque 

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

    def bfs(self): 
        nodes = [] 
        if self.root is None: 
            print("Tree is Empty") 
            return 
        
        queue = deque([self.root]) 
        
        while len(queue) > 0: 
            temp = queue.popleft() 
            nodes.append(temp.data) 
            
            if temp.left: 
                queue.append(temp.left) 
            if temp.right: 
                queue.append(temp.right) 
        
        return nodes


# Main Program
b = bst() 

while True: 
    choice = int(input("\n1. INSERT \t 2. BFS Traversal \t 3. EXIT\nEnter your choice: ")) 
    
    if choice == 1: 
        item = int(input("Enter element to insert into Tree: ")) 
        b.insert(node(item)) 
        
    elif choice == 2: 
        print("BFS traversal is:", b.bfs())           
        
    elif choice == 3:
        print("Exiting...")
        break
        
    else: 
        print("Invalid choice! Try again.")