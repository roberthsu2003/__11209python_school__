import random

class Player:
#attribute
    def __init__(self, name:str):
        self.name = name
#method
    def __play(self):
        score = ''
        while score == '':   
            dice1 = random.randint(1,6)
            dice2 = random.randint(1,6)
            dice3 = random.randint(1,6)
            dice4 = random.randint(1,6) 
            D = sorted([dice1, dice2, dice3, dice4])
            if (D[0] == D[1] == D[2] == D[3]):             #相當於(D[0] == D[1]) & (D[1] == D[2]) & (D[2] == D[3])  
                score = D[0] + 12
            elif (D[0] != D[1] != D[2] != D[3]):           #相當於(D[0] != D[1]) & (D[1] != D[2]) & (D[2] != D[3])  
                score = ''
            elif (D[0] == D[1] == D[2]) or (D[1] == D[2] == D[3]): #相當於[(D[0] == D[1]) & (D[1] == D[2])] or 
                score = ''                                         #     [(D[1] == D[2]) & (D[2] == D[3])]
            else:
                if D[0] == D[1]:
                    score = D[2] + D[3]
                elif D[1] == D[2]:
                    score = D[0] + D[3]
                elif D[2] == D[3]:
                    score = D[0] + D[1] 
        
        return f'骰子一:{dice1} 骰子二:{dice2} 骰子三:{dice3} 骰子四:{dice4}\n{D}\n得分:{score}'

#property
    @property
    def value(self):
        return self.__play()

#被呼叫時傳出字串
    def __repr__(self) -> str:
        descript = f"姓名:{self.name}"
        return descript

p1 = Player('甲')
print(p1)
print(p1.value)
print()
p2 = Player('乙')
print(p2)
print(p2.value)