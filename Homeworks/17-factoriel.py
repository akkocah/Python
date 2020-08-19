number = input ("enter the number : ")

result = 1
while True:
    if number.isdigit():        
        for i in range(int(number)):
            result += i*result
           
        print(result)
        break
    else: 
        print("It is invalid entry. Don't use non-numeric numbers")
        break
