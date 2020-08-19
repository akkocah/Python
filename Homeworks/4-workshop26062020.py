#Kullanıcıdan aldığın 3 sayıyı al çarp
# sayi1 = int(input("Birinci sayıyı giriniz :"))
# sayi2 = int(input("İkinci sayıyı giriniz :"))
# sayi3 = int(input("Üçüncü sayıyı giriniz :"))

# carpım = sayi1 * sayi2 * sayi3
# print("Girdiğiniz sayıların çarpımı :", carpım)
# print("Girdiğiniz sayıların çarpımı = {}*{}*{}={}".format(sayi1,sayi2,sayi3,carpım))
# print(f"Girdiğiniz sayıların çarpımı {sayi1}*{sayi2}*{sayi3}={carpım} dır")
# print("Girdiğiniz üç sayının çarpımı %d dir" %(carpım))

##Kullanıcıdan aldığımız boy kilo

# kilo = int(input("Kilonuzu Giriniz :"))
# boy = int(input("Boyunuzu cm olarak giriniz :"))
# boy = boy / 100
# bki = kilo / boy ** 2

# print("Beden kitle endeksiniz : ", round(bki,2))

# # Elinizde 200 dolarla değeri 11 olan malzemeden kaçtane alabiliriz
# money = 200
# malz_deger = 11
# max_adet = money // malz_deger  #flor divisions
# kalan_para = money % malz_deger
# print("{} dolar ile alabileceğiniz maks malzeme {} dir. geriye {} dolar kalır.".format(money,max_adet,kalan_para))

# kullanıcıdan iki sayı al değerlerini birbiriyle değiştir
# a = int(input("birinci sayıyı giriniz  :"))
# b = int(input("ikinci sayıyı giriniz :"))

# print("değiştirilmeden önceki değerler :\na={} b={}".format(a,b))
# a,b = b,a

# print("değiştirildikten sonraki  değerler :\na={} b={}".format(a,b))
# print(f"değiştirildikten sonraki değerler : \na={a} b={b}")

# # kullanıcıdan ad soy ad al 
# ad = input("adınızı giriniz :")
# soyad = input("soyadınızı giriniz :")
# num = int(input("telefon numarasınızı giriniz :"))

# print("Ad:\t {}\nSoyad:\t {}\nTelefon: {}".format(ad,soyad,num))

# KUllanıcıdan word 
# word = input('Word : ')
# seperator = input('Seperator:')
# repetitions = int(input('Repetition'))

# a = (word + seperator)*(repetitions-1)+word
# print(a)
#kullanıcıdan kelime ve sayı girdisi al
# word = input("Word  :")
# n = int(input("repetition of the last n charecter :"))
# a = len(word)
# #b = word[a-n:]
# b = word[-n:]
# print(a)
# print(b)
# print(b*n) #n sayısı kadar yazar
#Kullanıcıdan sayıı alın eğer sayı 3 e bölünüyorsa clarus
# 5 e bölünürse way her ikisine bölünürse clarusway yazsın ikisinide bölünmüyorsa 
#sayıyı yazdırsın

# num = int(input("Bir sayı girin :"))
# print(num % 3 == 0)#True bu eşitlik 
# print(num % 5 == 0) #True
# print('Clarus' * (num % 3 == 0)+ 'way' * (num % 5 == 0) or num)

#
# Letters = "abcclarusxyz"
# print(Letters[2:-3])
# print(Letters[2::-1])
# print(Letters[:-9:-1])

# Problem 10
# rand_list listesinin elemanlarından Claruway is the best yazdırın
# rand_list = [1,[1, 2, "Clarus", [2, "way"]], " is the best"]
# print(rand_list[1][2] + rand_list[1][3][1] + rand_list[2])

# Problem 11
# Aşağıda verilen listeyi küçükten büyüğe sıralayın. 
# 1 den 10 a kadar eksik olan sayıyı bulun?
# num_list = [2, 3, 1, 5, 6, 4, 9, 8, 10]
# a = sorted(num_list)
# print(a)
# list1 = set(a)
# list2 = set(range(1,11))
# print(list2)
# list_mis = list2.difference(list1)
# print(list_mis)

# Problem 12
# en yaşlı kişinin ismini yazdırın?

# old ={
#   "Emma": 71,
#   "Jack": 45,
#   "Amy": 15,
#   "Ben": 29
# }
# print(old)
# print(max(old, key=old.get))
##denemeler

# list1 = [3,1,4,6]
# list1.sort()
# list1.reverse()
# print(list1)

# my_list = list(range(11,1))
# my_list.reverse()
# print(my_list)

# grocer = ["banana", ["orange", ["apple", "eggplant", "melon", "spinach", "cheese", "leek" ], "water"], "mandarin"]

# print(grocer[1][1][1::2])
#############################################33

# text1 = "My two favorite flowers are tulip and rose, two favorite colors are blue and green."
# flowers = [["jasmine", ["lavender", "rose"], "tulip"]]
# colors = ["red", ("blue", ["yellow", "green"]), "pink"]
# text = "My two favorite flowers are {} and {}, two favorite colors are {} and {}. " \
#         .format(flowers[0][2],flowers[0][1][1],colors[1][0],colors[1][1][1])
# print(text)

########################333333
sentence = "I am 40 years old.{} I have two children.{} Data Science is my IT domain."\
        .format("\n\t","\n\t\t")

print(sentence)

