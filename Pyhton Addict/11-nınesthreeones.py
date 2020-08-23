class ones_threes_nines:

    def __init__(self, number):
        self.number = number
        #self.nines = number // 9
        self.answer = f"nines: {number // 9}, threes: {(number-(number//9)*9)//3}, ones : {(number-(number//3)*3)}"
        

p1 = ones_threes_nines(26)
print(p1.answer)

class ones_threes_nines:
    def __init__(self, answer):
        self.answer= 'nines:{}, threes:{}, ones:{}'.format(answer//9, (answer-(answer//9)*9)//3, answer-(answer//3)*3)

p1 = ones_threes_nines(26)
print(p1.answer)