sentence = input("Enter Sentence :").replace(" ","")

liste = list(sentence)
#print(set(liste))
mydict = {}

for i in liste:
    if i in mydict:
        mydict[i] +=1
    else:
        mydict[i] = 1

print(f"Coun of the chars of your sentences are : {mydict}")
print()
print(f"Coun of the chars of your sentences are : {mydict.items()}")

print("Your sentence has  :"  )
for key, value in mydict.items() :
    print (key, ":", value)


# sentence = list(input("Give me a sentence!"))
# length = len(sentence)
# dict1 = {}
# for i in range(length):
#     count = 0    for j in range(length):
#         if sentence[i] == sentence[j]:
#             count +=1
#             dict1[sentence[i]] = count
# print(dict1)

