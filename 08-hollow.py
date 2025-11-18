n = int(input())

# top side
for row in range(1, n+1):
    
    for j in range(n - row):
        print('*', end='')
        
 
    for k in range(2*row - 1):
        print(' ', end='')
    

    for j in range(n - row):
        print("*", end='')
    print()
    
# bottom side
for row in range(n-1,0,-1):
  
    for j in range(n-row):
        print('*',end='')
    
    for k in range(2*row-1):
        print(" ",end='')
        
    for j in range(n-row):
        print('*',end='')
    print()
    