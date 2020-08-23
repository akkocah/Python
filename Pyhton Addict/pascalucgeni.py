def pascal(row):
    newList=list()
    numbers=[[1],[1,1]]
    for i in range(2,row):
        newList.append (1)
        for j in range(i-1):
            newList.append (numbers[i-1][j]+numbers[i-1][j+1])
        newList.append(1)
        numbers.append(newList)
        newList=[]
    for index,number in enumerate(numbers):
        print('  '*len(numbers[row-index-1])+("{:^5}"*len(number)).format(*number))
pascal(10)

def pascal1(row):
    if row==1:
        return [1]
    else:
        x=[1]
        a=pascal1(row-1)
        for i in range(0,len(a)-1):
            x.append(a[i]+a[i+1])
        x+=[1]    
    return x        
print(pascal1(20))