count=0 
def toh(n , source, destination, temp): 
    if n==1: 
        print ("Move disk 1 from source",source,"to ",destination) 
        global count 
        count=count+1 
        return 
    toh(n-1, source, temp, destination) 
    print ("Move disk",n,"from source",source,"to ",destination) 
    count=count+1 
    toh(n-1, temp, destination, source) 
          
n = int(input("Enter number of disks")) 
toh(n,'A','B','C') 
print("total number of moves",count) 