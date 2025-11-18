def pyramid(n):
    for i in range(1,n+1):
        #Printing leading spacce
        for j in range(n - i):
            print(' ',end='')
        #printing pattern
        for k in range(1,2*i):
            print("*",end='')
        print()

pyramid(5)