def fib(n): 
  if n == 0 or n==1: 
      return n 
  else: 
      return(fib(n-1) +fib(n-2)) 
 
def fact(n): 
  if n == 0 or n==1: 
      return 1 
  else: 
      return n*fact(n-1) 
     
n=int(input("Enter value for n")) 
print("Fibonacci series of",n) 
for i in range(n+1): 
    print(fib(i),end=',') 
 
print("\n Factorial of",n) 
print(fact(n))