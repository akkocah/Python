
    # An n-digit number that is the sum of the nth powers of its 
    # digits is called an n-Armstrong number. Examples :

    # 371 = 33 + 73 + 13;
    # 9474 = 94 + 44 + 74 + 44;
    # 93084 = 95 + 35 + 05 + 85 + 45.

    # Sample inputs 	Outputs
    #     407 	        407 is an Armstrong number
    # 5 	            5 is an Armstrong number
    # 153 	     Please enter a positive number
    # 153.87 or 153,87 	 Please enter an integer number
    # one 	    Do not use any entries other than numeric values
    # 121 	    121 is not an Armstrong number
# while True:
#     num = input("Enter a number:  ")
#     if num.isalpha():
#         print("Do not use any entries other than numeric values")
    
#     elif (".")  in list(num):
#         print("Please enter an integer number")

#     elif (",") in list(num):
#         print("Please enter an integer number")
#     elif int(num) < 0:
#         print("Please enter a positive number")     

#     else:
        
#         break
# num = int(num)

# #num = int(input("Enter a number: "))  
# n = len(str(num))
# sum = 0  
# temp = num  
      
# while temp > 0:  
#     digit = temp % 10
      
#     sum += digit ** n
     
#     temp //= 10
    
      
# if num == sum:  
#    print(num,"is an Armstrong number")  
# else:  
#    print(num,"is not an Armstrong number")  

while True:
    sayi = input("Enter a number :  ")
    if sayi.isalpha():
        print("Do not use any entries other than numeric values")
    
    elif (".")  in list(sayi):
        print("Please enter an integer number")

    elif (",") in list(sayi):
        print("Please enter an integer number")
    elif int(sayi) < 0:
        print("Please enter a positive number")     

    else:
        
        break
sayi = int(sayi)


basamak = str(sayi)

toplam=0

for x in basamak:
    
    rakam = int(x)**len(basamak)
    toplam += rakam
    
    
if(sayi == toplam):
    print(f"{sayi} Bir Armstrong Sayısıdır.")
else:
    print(f"{sayi} Bir Armstong Sayısı Degildir.")