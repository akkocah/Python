# for i in range(1,11):
    
#     for j in range(1,11):        
        
#         if j == 10:
#             print(str(j*i ).rjust(4),"\n")
#         else:
#             print(str(j*i ).rjust(4), end = "  " )


for i in range(1,11):
    
    for j in range(1,11):        
        
        if j == 10:
            
            print('{:5d}'.format(j*i), "\n " )
        else:
            print('{:5d}'.format(j*i), end = " " )

# for sıra, karakter in enumerate(dir(str)):
#     if sıra % 3 == 0:
#         print("\n", end="")
#     print("{:<30}".format(karakter), end="")

for i in range(1, 11):
    for j in range(1, 11):
        print(f"{i*j:4d}", end = " ")
    print()

for i in range(1, 11):
    for j in range(1, 11):
        print(("{:6d}".format(i * j)), end='')
    print()
        