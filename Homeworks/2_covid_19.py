#!/usr/bin/env python
# -*- coding: utf-8 -*- 
age = input("Are you a cigarette addict older than 75 years old? True or False :")
chronic = input("Do you have a severe chronic disease? True or False :")
immune = input("Is your immune system too weak? True or False :")

if age.lower() == "true" or chronic.lower() == "true" or immune.lower() == "true":
    print ("there is a risk of death")
else:
    print ("there is not a risk of death")

while True:
    while True:
        age = input("Are you a cigarette addict older than 75 years old? True or False :")
        if age.lower() =="true":
            age = True
            break
        elif age.lower() == "false":
            age = False
            break
        elif age.lower() != "true" or "false":
            print("lütfen 'True' yada 'false' olarak giriniz")
            break
    while True:
        chronic = input("Do you have a severe chronic disease? True or False :")
        if chronic.lower() =="true":
            chronic = True
            break
        elif chronic.lower() == "false":
            chronic = False
            break
        elif chronic.lower() != "true" or "false":
            print("lütfen 'True' yada 'false' olarak giriniz")
            break
    while True:
        immune = input("Is your immune system too weak? True or False :")
        if immune.lower() =="true":
            immune = True
            break
        elif immune.lower() == "false":
            immune = False
            break
        elif immune.lower() != "true" or "false":
            print("lütfen 'True' yada 'false' olarak giriniz")
            
    if age or immune or chronic ==True:
        print("there is a risk of death")
    else:
        print("there is not a risk of death")
    break

# class color:
#     PURPLE = '\033[95m'
#     CYAN = '\033[96m'
#     DARKCYAN = '\033[36m'
#     BLUE = '\033[94m'
#     GREEN = '\033[92m'
#     YELLOW = '\033[93m'
#     RED = '\033[91m'
#     BOLD = '\033[1m'
#     UNDERLINE = '\033[4m'
#     END = '\033[0m'
# while True:
#     while True:
#         age = input("Are you a " + color.BLUE + "cigarette " + color.END + "addict older than " + color.BOLD + "75 " + color.END + "years old? True or False: ")
#         if age.lower() == "true":
#             age = True
#             break
#         elif age.lower() == "false":
#             age = False
#             break
#         elif age.lower() == "true" or "false":
#             print("Try again and be carreful !!!")
#     while True:
#         chronic = input("Do you have a " + color.BOLD + "severe " + color.END + "chronic disease? True or False?: ")
#         if chronic.lower() == "true":
#             chronic = True
#             break
#         elif chronic.lower() == "false":
#             chronic = False
#             break
#         elif chronic.lower() == "true" or "false":
#             print("Try again and be carreful !!!")
#     while True:
#         immune = input("Is your " + color.BOLD + "immune " + color.END + "system " + color.BOLD + "too weak" + color.END + "? True or False?: ")
#         if immune.lower() == "true":
#             immune = True
#             break
#         elif immune.lower() == "false":
#             immune = False
#             break
#         elif immune.lower() == "true" or "false":
#             print("Try again and be carreful !!!")
#     risk = age or chronic or immune
#     if risk == True:
#         print("There is a risk of death")
#     elif risk == False:
#         print("There is not a risk of death")
#     break