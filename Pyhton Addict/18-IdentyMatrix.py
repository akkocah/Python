def id_mtrx(n):
    if type(n) == int:
        if n > 0:
            array = [[0]*n for i in range(n)]
            for i in range(n):
                array[i][i] = 1
        elif n < 0:
            array = [[0]*(n*-1) for i in range((n*-1))]
            for i in range(len(array)):
                for j in range(len(array)):
                    if (i+j) == (len(array)-1):
                        array[i][j] = 1
        return array
        
    else:
        return 'Error'
print(id_mtrx(8))

# def id_mtrx(n):
#     if not type(n) == int: return 'Error'
#     s = 1 if n >= 0 else -1
#     return [[1 if i == j else 0 for i in range(abs(n))] 
# 						for j in range(abs(n))][::s]

# def id_mtrx(n):
#     if type(n) == int:
#         a=[0 for i in range(abs(n)) ]
#         b=[]
#         for i in range(abs(n)):
#             if n > 0:
#                 c=a.copy()
#                 c[i] = 1
#                 b.append(c)
#             else:
#                 c=a.copy()
#                 c[-i-1] = 1
#                 b.append(c)
#         return b
#     else :
#         return "Error"

# print(id_mtrx(4))