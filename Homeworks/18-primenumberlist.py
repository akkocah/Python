
#  The desired output for n=100 :

# [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59,
# 61, 67, 71, 73, 79, 83, 89, 97]

number = int(input("Enter the number : "))
list_prime = [1]

for i in range(2,number):
    is_prime = True
    for j in range(2,i):
        if i % j == 0:
            is_prime = False
    if is_prime:
        list_prime.append(i)
print(f"The prime number lists = {list_prime}") 
