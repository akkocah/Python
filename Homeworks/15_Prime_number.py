num = int(input("Enter your number please : "))
isprime = True

if num == 1:
   isprime = False

for i in range(2, num):
    if num % i == 0:
        isprime = False
        break 
if isprime == False:
    print(f"{num} is not a prime number")
else:
    print(f"{num} is a prime number")


# number = int(input("Enter a number: "))
# if number > 1 :
#     for i in range(2, number) :
#         if number % i == 0 :
#             print(number, "is not a prime number.")
#             break
#         else :
#             print(number, "is a prime number.")
#             break
# else :
#     print(number, "is not a prime number.")
        
    