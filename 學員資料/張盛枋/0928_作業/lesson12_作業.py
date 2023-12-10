import random

class Player:
#attribute
    def __init__(self, name:str):
            self.name = name
    name:str
    __dice1:int(1-6)
    __dice2:int(1-6)
    __dice3:int(1-6)
    __dice4:int(1-6)

#method
    def __play(self):
        score = 0
        while score == 0:
            MatchCnt = 0
            ScoreTemp = 0 
            __dice1 = random.randint(1,6)
            __dice2 = random.randint(1,6)
            __dice3 = random.randint(1,6)
            __dice4 = random.randint(1,6)
            # 測試用
            '''
            __dice1 = 1
            __dice2 = 1
            __dice3 = 1
            __dice4 = 1
            '''
            DiceList = [__dice1, __dice2, __dice3, __dice4]
            for i in range(3):
                for j in range(i+1,4) :
                    if DiceList[i] == DiceList[j] :
                        MatchCnt+= 1
                        ScoreTemp += DiceList[i]
            if MatchCnt == 1 :
                score = sum(DiceList)-ScoreTemp*2
            elif  MatchCnt == 2:
                score = max(DiceList)*2
            elif MatchCnt == 6:
                score = DiceList[0] + 12
            else :
                score = 0        
        return (f' 骰子1: {__dice1}\n 骰子2: {__dice2}\n 骰子3: {__dice3}\n 骰子4: {__dice4}\n 得分:  {score}')

#property
    @property
    def value(self):
        return self.__play()

#回傳姓名
    def __repr__(self) -> str:
        PlayerName = f"姓名: {self.name}"
        return PlayerName

p1 = Player('玩家1')
print(p1)
print(p1.value ,'\n')

p2 = Player('玩家2')
print(p2)
print(p2.value)