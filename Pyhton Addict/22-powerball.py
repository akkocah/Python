from random import randint
whitenumbers = set()
while len(whitenumbers) <5:
    whitenumbers.add(randint(1,69))
whitenumbers = list(whitenumbers)
whitenumbers.sort()
powerballnumber = randint(1,26)
for i in whitenumbers:
    print(i,end=' ')
print(f" + {powerballnumber}")