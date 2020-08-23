def print_table(start,col):   
    for i in range(1,11):
        row = []
        for j in range(start,start+col):
            row.append(f"{j:2d} x {i:2d} = {i*j:2d}")
        print("   ".join(row))
col = int(input("In how many columns do you want to see multiplication table : "))
div = 10 // col
remainder = 10 % col
for i in range(div):
    print_table(1+i*col,col)
    print()
if remainder !=0:
    print_table(div*col+1,remainder)

# for i in range(1,11):   # fonksiyonun içine bu şekilde yazılabilir.
#         for j in range(start,start+col):
#             print(f"{j:2d}x{i:2d} = {i*j:2d}   ",end='')
#         print()

# for i in range(11):
#     for j in range(11):
#         print(f"{i} x {j:2d} = {i*j} ", end ="\t")
#     print()

# for i in range(2):
    
#     for j in range(11):
#         #print(row*col, "\t",end = "") 
#         print(f"{i} x {j:2d} = {i*j} ","\n", end ="")     
#     print("***********")

# # for row in range(1, 11):
# #     for col in range(1, 11):
# #         num = row * col
# #         if num < 10: blank = '  '       # 2 blanks
# #         else:
# #             if num < 100: blank  = ' '  # 1 blank
# #         print(blank, num, end = '')     # Empty string
# #     print() 

# # for x in range(1, 11):
# #         for y in range(1, 11):
# #             z = x * y
# #             print(z, end="\t")
# #         print() #creates the space after the loop


# # for i in range(1, 11):
# #     for j in range(1, 11):
# #         print(("{:6d}".format(i * j)), end='')
# #     print()

