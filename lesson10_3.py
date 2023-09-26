import random
import pyinputplus as pyip

def playGame():
    min = 1
    max = 100
    count = 0
    target = random.randint(min, max)
    print(target)
    print("===============猜數字遊戲=================:\n")
    while(True):
        count += 1
        keyin = int(input(f"猜數字範圍{min}~{max}"))
        if (1 <= keyin <= max):
            if(keyin == target):
                print(f"賓果!猜對了, 答案是:{target}")
                print(f"總共猜了{count}次")
                break
            elif (keyin > target):
                print("再小一點")
                max = keyin - 1
                
            elif (keyin < target):
                print("再大一點")
                min = keyin + 1
                
            print(f"您已經猜了{count}次")
        else:
            print("請輸入提示範圍內的數字")


while True:
    playGame()
    answer = pyip.inputYesNo(prompt="還要繼續嗎?(y,n)",yesVal='y',noVal='n')
    if not (answer == 'y'):
        break
print("遊戲結束")
    