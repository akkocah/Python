
number = int(input("sayıyı giriniz :"))

liste = []
a = 0  
b = 1 
while (a < number):
     c = b  
     b = a  
     a = c + b  
     liste.append(a)
print(liste)

number = 55
fibonacci = []
a = 0
b = 1
while (a < number):
     c, b = b, a
     a = c + b
     fibonacci.append(a)
print(fibonacci)









