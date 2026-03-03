# Define a class named stack
class stack: 
    
    # Constructor method - initializes an empty list to represent the stack
    def __init__(self): 
        self.stack = []   # Stack is implemented using Python list
         
    # Method to return the number of elements in the stack
    def length(self): 
        return len(self.stack)   # len() gives total elements in list
     
    # Method to insert (push) an element into the stack
    def push(self, item): 
        self.stack.append(item)  # append() adds element at the top (end of list)
         
    # Method to remove (pop) an element from the stack
    def pop(self): 
        # Check if stack is empty
        if len(self.stack) == 0: 
            return "Stack is empty"   # Cannot pop from empty stack
        else: 
            return self.stack.pop()   # pop() removes last element (LIFO principle)
     
    # Method to display elements of stack
    def display(self): 
         # Check if stack is empty
         if len(self.stack) == 0: 
            return "Stack is empty" 
         else:         
            return self.stack   # Returns complete stack list
     

# Creating an object of stack class
s = stack() 

# Infinite loop to repeatedly show menu
while True:   # Better than while 1
    
    # Menu driven program
    choice = int(input("\n1.PUSH \t 2.POP \t 3.DISPLAY \t 4.LENGTH \t 5.EXIT\n")) 
    
    # If user selects PUSH
    if choice == 1: 
        item = input("Enter element to push into stack: ") 
        s.push(item)   
        
    # If user selects POP
    elif choice == 2: 
        print("Popped element is:", s.pop()) 
        
    # If user selects DISPLAY
    elif choice == 3: 
        print("Elements in stack:", s.display()) 
        
    # If user selects LENGTH
    elif choice == 4: 
        print("Number of elements in stack:", s.length()) 
        
    # If user selects EXIT
    elif choice == 5:  
        print("Exiting program...")
        break   # 🔹 Stops the loop
        
    # If user enters invalid choice
    else:
        print("Invalid Choice! Please select between 1 to 5.")