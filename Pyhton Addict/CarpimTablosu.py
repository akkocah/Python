

n = int(input("In how many columns do you want to see multiplication table: "))

if n == 1:
    for j in range(1,11):
        for i in range(1,11):
            print(f"{j} x {i} = {i*j}")
        print()
    print()

elif n==2:
    for j in range(1,11):
        for i in range(1,n+1):
            print("%-2d x %2d = %3d"%(i,j,i*j), end = "   ")
        print()
    print()
    
    for j in range(1,11):
        for i in range(n+1,2*n+1):
            print("%-2d x %2d = %3d"%(i,j,i*j), end = "   ")
        print()
    print()
    
    for j in range(1,11):
        for i in range(2*n+1,3*n+1):
            print("%-2d x %2d = %3d"%(i,j,i*j), end = "   ")
        print()
    print()
    
    for j in range(1,11):
        for i in range(3*n+1,4*n+1):
            print("%-2d x %2d = %3d"%(i,j,i*j), end = "   ")
        print()
    print()
    
    for j in range(1,11):
        for i in range(4*n+1,11):
            print("%-2d x %2d = %3d"%(i,j,i*j), end = "   ")
        print()
    print()

elif n == 3:
    
    for j in range(1,11):
        for i in range(1,n+1):
            print("%-2d x %2d = %3d"%(i,j,i*j), end = "   ")
        print()
    print()
    
    for j in range(1,11):
        for i in range(n+1,2*n+1):
            print("%-2d x %2d = %3d"%(i,j,i*j), end = "   ")
        print()
    print()
    
    for j in range(1,11):
        for i in range(2*n+1,3*n+1):
            print("%-2d x %2d = %3d"%(i,j,i*j), end = "   ")
        print()
    print()
    
    for j in range(1,11):
        for i in range(3*n+1,11):
            print("%-2d x %2d = %3d"%(i,j,i*j), end = "   ")
        print()
    print()
    
elif n == 4 :
    for j in range(1,11):
        for i in range(1,n+1):
            print("%-2d x %2d = %3d"%(i,j,i*j), end = "   ")
        print()
    print()

    for j in range(1,11):
        for i in range(n+1,2*n+1):
            print("%-2d x %2d = %3d"%(i,j,i*j), end = "   ")
        print()
    print()
        
    for j in range(1,11):
        for i in range(2*n+1,11):
            print("%-2d x %2d = %3d"%(i,j,i*j), end = "   ")
        print()
    print()
    
else:    
    for j in range(1,11):
        for i in range(1,n+1):
            print("%-2d x %2d = %3d"%(i,j,i*j), end = "  ")
        print()
    print()

    for j in range(1,11):
        for i in range(n+1,11):
            print("%-2d x %2d = %3d"%(i,j,i*j), end = "  ")
        print()
    print()


# In[ ]:




