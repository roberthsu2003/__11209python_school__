import random


class FourDice:
    def __init__(self, name: str):
        self.__dice1 = random.randint(1, 6)
        self.__dice2 = random.randint(1, 6)
        self.__dice3 = random.randint(1, 6)
        self.__dice4 = random.randint(1, 6)
        self.name = name

    def play(self):
        V = sorted([self.__dice1, self.__dice2, self.__dice3, self.__dice4])
        score=''
        if V[0] == V[1] == V[2] == V[3]:
            score = V[0]+12
        elif (V[0] != V[1] != V[2] != V[3]) or (V[0] == V[1] == V[2] != V[3]) or (V[1] == V[2] == V[3] != V[0]):
            score = 0 #想了三天，不知道怎麼重來………
        elif V[0] == V[1]:
            score = V[2]+V[3]
        elif V[1] == V[2]:
            score = V[0]+V[3]
        elif V[2] == V[3]:
            score = V[0]+V[1]
        return score
       
    @property
    def value(self):
        return self.play()

    def __str__(self) -> str:
        descript = ""
        descript += f'玩家姓名:{self.name}\n'
        descript += f'Dice1={self.__dice1}\n'
        descript += f'Dice1={self.__dice2}\n'
        descript += f'Dice1={self.__dice3}\n'
        descript += f'Dice1={self.__dice4}\n'
        descript += f'得分={self.value}'
        return descript


h1 = FourDice("kimi")
print(h1)

h2 = FourDice('Tina')
print(h2)

