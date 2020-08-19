
    # Task : Print the FizzBuzz numbers.
    # FizzBuzz is a famous code challenge used in interviews to test basic programming skills. 
    # It's time to write your own implementation.

    # Print numbers from 1 to 100 inclusively following these instructions:

    # if a number is multiple of 3, print "Fizz" instead of this number,
    # if a number is multiple of 5, print "Buzz" instead of this number,
    # for numbers that are multiples of both 3 and 5, print "FizzBuzz",
    # print the rest of the numbers unchanged.

numbers = list(range(1,100))
list1=[]

for i in (numbers):

    if (i % 5 == 0) and (i % 3 == 0):
        result = "FizzBuzz"
        list1.append(f"{i} = {result}")
    elif i % 3 == 0:
        result = "Fizz"
        list1.append(f"{i} = {result}")
    elif i % 5 == 0:
        result = "Buzz"
        list1.append(f"{i} = {result}")
    else:
        result = i
    print((result))
print(list1)

# number_list=[]
# for i in range(1, 101):
#     if i % 15 == 0:
#         number_list.append("FizzBuzz")
#     elif i % 3 == 0:
#         number_list.append("Fizz")
#     elif i % 5 == 0:
#         number_list.append("Buzz")
#     else:
#         number_list.append(i)
# for i in number_list:
#     print(i, sep="\n") 
