# https://edabit.com/challenge/9iLhKgqZn5exBrmWm
#  Notes
# A number can consist of any number of digits, so long as the numbers are adjacent to each other, and the string has at least two of them.Test.assert_equals(ascending("232425"), True)
# Test.assert_equals(ascending("444445"), True)
# Test.assert_equals(ascending("1234567"), True)
# Test.assert_equals(ascending("123412351236"), True)
# Test.assert_equals(ascending("57585960616263"), True)
# Test.assert_equals(ascending("500001500002500003"), True)
# Test.assert_equals(ascending("919920921"), True)
# Test.assert_equals(ascending("2324256"), False)
# Test.assert_equals(ascending("1235"), False)
# Test.assert_equals(ascending("121316"), False)
# Test.assert_equals(ascending("12131213"), False)
# Test.assert_equals(ascending("54321"), False)
# Test.assert_equals(ascending("56555453"), False)
# Test.assert_equals(ascending("90090190290"), False)
# Test.assert_equals(ascending("35236237238"), False) 

# A=‘444445’
# for i in range(1,len(A)//2+1):
#     k,B,C=0,[],[]
#     for j in range(len(A)):
#         if len(A[k:k+i])==i and len(A[k+i:k+2*i])==i:
#             C.append([A[k:k+i],A[k+i:k+2*i]])
#             B.append(int(A[k:k+i])+1==int(A[k+i:k+2*i]))
#             k=k+i
#     if all(B) and C[-1][-1][-1]==A[-1]:
#         print(True)
#         break
# else:
#     print(False)

def ascending ( txt ) :
    splitted=[split_txt(txt,step) for step in range(1,len(txt)//2+1)]
    return any([is_iterate(txt) for txt in splitted])
def split_txt(txt,step):
    ch,s,splited='',step,[]
    for i in txt:
        ch+=i;s-=1
        if not s: splited.append(ch);ch,s='',step
    if ch!='': splited.append(ch)
    return splited
def is_iterate(txt):
    start,boolList=int(txt[0]),[]
    for i in txt[1:]:
        if int(i)!=start+1: return False
        else: start=int(i)
    return True

print(ascending("121314"))