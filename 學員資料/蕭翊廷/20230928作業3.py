import random
import statistics

class Player:
    def __init__(self, name):
        self.__dice1 = 0
        self.__dice2 = 0
        self.__dice3 = 0
        self.__dice4 = 0
        self.name = name

    def __play(self) -> int:
        Dice = [self.__dice1, self.__dice2, self.__dice3, self.__dice4]

        if len(set(Dice)) == 1:
            dict={0:0,1:13,2:14,3:15,4:16,5:17,6:18}
            score=dict.get(Dice[0])
        elif len(set(Dice)) == 4:
            score = 0
        elif Dice.count(Dice[0]) == 3 or Dice.count(Dice[1]) == 3:      #不能寫成Dice.count(Dice[0]) or Dice.count(Dice[1]) == 3
            score = 0                                                   #一定要分別寫 == 3
        else:
            score = sum(Dice) - min(statistics.multimode(Dice)) * 2

        return score

    @property
    def value(self) -> int:
        return self.__play()

    def roll_dice(self):
        self.__dice1 = random.randint(1, 6)
        self.__dice2 = random.randint(1, 6)
        self.__dice3 = random.randint(1, 6)
        self.__dice4 = random.randint(1, 6)

    def __repr__(self) -> str:
        descript = ""
        descript += f"{self.name}\n"
        descript += f"骰子1={self.__dice1}\n"
        descript += f"骰子2={self.__dice2}\n"
        descript += f"骰子3={self.__dice3}\n"
        descript += f"骰子4={self.__dice4}\n"
        descript += f"得分={self.value}分"
        return descript

def main():
    p1 = Player("Robert")
    p2 = Player("John")

    while p1.value == 0:
        p1.roll_dice()
    while p2.value == 0:
        p2.roll_dice()

    print(p1)
    print(p2)

    print("遊戲结束")

if __name__ == "__main__":
    main()