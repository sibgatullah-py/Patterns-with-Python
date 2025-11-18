n = int(input())
for row in range(n, 0, -1): # row starts at n biggest level and ends at 1 lowest level
    #space
    for j in range(n-row):
        print(' ',end="")
    
    #star
    for k in range(2*row-1):
        print('*', end="")
    print() # next row