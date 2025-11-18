n = int(input())

# top side
for row in range(1,n+1):
    #space
    for j in range(n-row):
        print(' ',end='')
    #star
    for k in range(2*row-1):
        print('*', end='')
    print()
    
# bottom side
for row in range(n-1,0,-1):
    #space
    for j in range(n-row):
        print(' ',end='')
    #star
    for k in range(2*row-1):
        print("*",end='')
    print()