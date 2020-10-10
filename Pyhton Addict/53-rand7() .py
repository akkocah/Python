# QUESTION:
# This is an interview question asked by Two Sigma.
# Using a function rand7() that returns an integer from 1 to 7 (inclusive) with uniform probability, implement a function rand5() that returns an integer from 1 to 5 (inclusive).
# Not: Aklınıza geldiği gibi çözün. Tuzak filan yok. Çekinmeden çözümünüzü gönderin lütfen.

from random import randint
def rand7():
    return randint(1,7)

def rand5():
    x = rand7()
    return x if 1 <= x <= 6 else rand5()

print(rand5())

def rand5_():
    x=rand7()
    while x<6:
        return x
    else:
        return rand5_()

print(rand5_())