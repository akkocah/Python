age = input("Are you a cigarette addict older than 75 years old? True or False :")
chronic = input("Do you have a severe chronic disease? True or False :")
immune = input("Is your immune system too weak? True or False :")

if (age.lower() == "true") or (chronic.lower() == "true") or (immune.lower() == "true"):
    print("You are in risky group")
elif (age.lower() == "false") and (chronic.lower() == "false") and (immune.lower() == "false"):
    print("You are not in risky group")
else:
     print("Yanlış giriş yaptınız.")

     