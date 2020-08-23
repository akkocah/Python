# def tournament_scores(s):
#     teams,score,goals,avar,output=set(),[],[],[],[]
#     for i in s:
#         item=i.split()
#         teams.update(item[0],item[-1])
#         score.append((item[0],3 if int(item[1])>int(item[-2]) else 1 if int(item[1])==int(item[-2]) else 0))
#         score.append((item[-1],0 if int(item[1])>int(item[-2]) else 1 if int(item[1])==int(item[-2]) else 3))
#         goals.append((item[0],int(item[1])))
#         goals.append((item[-1],int(item[-2])))
#         avar.append((item[0],int(item[1])-int(item[-2])))
#         avar.append((item[-1],int(item[-2])-int(item[1])))
#     teams=sorted(list(teams))
#     for t in teams:
#         x,y,z=[0,0,0]
#         for s in score:
#             if s[0]==t: x+=s[1]
#         for g in goals:
#             if g[0]==t: y+=g[1]
#         for a in avar:
#             if a[0]==t: z+=a[1]
#         output.append([t,x,y,z])
#     return sorted(output,key=lambda x:x[1:],reverse=True)
# print(tournament_scores(["A 0 - 1 B", "C 2 - 0 D", "B 2 - 2 C", "D 3 - 1 A", "A 2 - 2 C", "B 2 - 0 D"]))
ps4_price = 99
while True:
    saved_amount = int(input('Please enter your saved amount: '))
    if saved_amount <= ps4_price/2:
        print("You must save more, keep saving!")
    elif saved_amount > ps4_price/2:
        print("You saved more than half, keep saving!")
    elif saved_amount > ps4_price:
        print("Yippee! You can buy your PS4")
        break