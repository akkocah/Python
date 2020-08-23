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