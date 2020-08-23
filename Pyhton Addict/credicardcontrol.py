# number = 7777777777777777
# A= list(str(number//10))[::-1]
# number1= list(map(lambda x : 2*int(x), A[::2]))
# number2= list(map(lambda x : x-9 if int(x)>9 else int(x), number1))
# K=list(map(lambda x : int(x), A[1::2]))
# print(((sum(K)+sum(number2))*9)%10==number%10)

##################################33333
def valid_credit_card(number):
    sayi = list(str(number)[::-1])
    for i in range(1, len(sayi),2):
        sayi[i] = int(sayi[i])*2
        if sayi[i] > 9: sayi[i] -= 9
    total = 0
    for i in sayi[1:]: total += int(i)
    return (total * 9)%10 == int(sayi[0])
print(valid_credit_card(1568795456895125))