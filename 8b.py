class bracket_matching: 

    # Constructor - initialize empty stack
    def __init__(self): 
        self.stack = []   # Stack implemented using list

    # Push method - adds element to stack
    def push(self, item): 
        self.stack.append(item) 

    # Pop method - removes element from stack
    def pop(self): 
        if len(self.stack) != 0: 
            return self.stack.pop()
        else:
            return None   # Return None if stack is empty
         
    # Bracket Matching function
    def bm(self, expr):         
        
        # Traverse each character in expression
        for ch in expr: 
            
            # If opening bracket → push into stack
            if ch in ('{', '[', '('): 
                self.push(ch) 
            
            # If closing bracket → check match
            elif ch in ('}', ']', ')'): 
                
                last = self.pop()  # Get last opening bracket
                
                # If stack was empty
                if last is None:
                    return False
                
                # Check matching pairs (use == not is)
                if last == '{' and ch == '}': 
                    continue 
                elif last == '[' and ch == ']': 
                    continue 
                elif last == '(' and ch == ')': 
                    continue 
                else: 
                    return False   # Not matching
        
        # After checking all characters
        # If stack still has elements → not balanced
        if len(self.stack) > 0: 
            return False 
        else: 
            return True 


# Create object
b = bracket_matching() 

# Take input expression
expr = str(input("Enter expression: ")) 

# Call bracket matching function
result = b.bm(expr) 

# Display result
if result == True: 
    print("Given expression is balanced") 
else: 
    print("Given expression is not balanced")