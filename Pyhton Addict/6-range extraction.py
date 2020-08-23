# solution([-6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20])
# # returns "-6,-3-1,3-5,7-11,14,15,17-20"
# def solution(*args):
#     new = []
#     for i in args:
#         if i + 1 != args.indx
#             new.append(i)
#         print(i)
#         print(args[i])
#     return new 

# solution([-6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20])  

l1=[-6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20]
#Output "-6,-3-1,3-5,7-11,14,15,17-20"
l2=[-5,-4,0,5,6,7,9,10]
#output: "-5,-4,0,5-7,9,10"
l3=[1,2,3,5,6,8,9,10,11]
#Output: "1-3,5,6,8-11"
prt=lambda b,e:"" if b==e else ("," if e==b+1 else "~")+str(e)
def reduce(v):
 beginr=endr=v[0]
 s=str(beginr)
 for x in v[1:]:
  if x!=endr+1:
   s=s+prt(beginr,endr)+","+str(x)
   beginr=x
  endr=x
 return(s+prt(beginr,endr))
    
for l in [l1]:
    print(reduce(l))