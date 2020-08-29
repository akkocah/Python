def fibo(x):
    if x == 1 or x == 2:
        return 1
    else:
        return (fibo(x-1)+fibo(x-2))
print(fibo(15))

def Fibo(n):
    fib = []
    fib.append(0)
    for i in range(-1,n):
        if i < 0 :
            fib.append(1)
        else: fib.append(fib[i]+fib[i+1])
    return fib
print(Fibo(15))
##############  Power of recursive
def power(x,y):
    if y == 1:
        return x
    else:
        return x * power(x,y-1)

print(power(2,1))

def power_of_x(x, y):
    return 1 if y <=0 else x * power_of_x(x, y-1)

print(power_of_x(2,0))

def exponet(x,y):
    return 1 if y <=0 else x if y == 1 else x * exponet(x, y-1)

print(exponet(8,1))

