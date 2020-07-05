#numbers = [1, 3, 7, 4, 3, 0, 3, 6, 3]
# Aşağıda kullanıcıdan sayıları istiyoruz split ile virgülden
#bölüyoruz. Sonuç otomatik olarak liste tipinde geldiği için 
# listeye çevirmeye gerek kalmıyor.
numbers = (input("Lütfen sayıları arasına virgül koyarak giriniz :")).split(",")
print(numbers, type(numbers))

most_frequent = max(numbers, key=numbers.count)
repeat_times = numbers.count(most_frequent)

print(f"The most frequent number is {most_frequent} and it was \
{repeat_times} times repeated")


print("The most frequent number is " + str(most_frequent) + " and it was " \
+ str(repeat_times) + " times repeated")