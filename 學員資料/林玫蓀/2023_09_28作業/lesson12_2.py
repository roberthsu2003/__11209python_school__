import random
import pyinputplus as pyip

class Player:
    def __init__(self, name:str):
        self.name = name
        self.__dice1 = 0
        self.__dice2 = 0
        self.__dice3 = 0
        self.__dice4 = 0
        self.point = 0

    def __play(self) -> int: 
        self.point = 0
        while self.point ==0:        
            self.__dice1 = random.randint(1, 6)
            self.__dice2 = random.randint(1, 6)
            self.__dice3 = random.randint(1, 6)
            self.__dice4 = random.randint(1, 6)         
            num = [self.__dice1, self.__dice2, self.__dice3, self.__dice4]   
               
            lt = []             
            for i in num :    
                lt.append(num.count(i))                     
            if sum(lt) ==4 or sum(lt) == 10 :
                self.point =0           
            elif sum(lt) == 6 :
                for j in range(4):
                    self.point += num[j] * (num.count(num[j])==1)      
            elif sum(lt) == 8 :
                self.point = max(num)*2
            else :
                self.point = num[0] + 12        
        #return point            
        
    @property
    def value(self)->int: 
        return self.__play()  
        
    def __repr__(self) ->str:
        descript = ""
        descript +=f"{self.name}\n"
        descript +=f"骰子1={self.__dice1}\n" 
        descript +=f"骰子2={self.__dice2}\n"
        descript +=f"骰子3={self.__dice3}\n"
        descript +=f"骰子4={self.__dice4}\n"
        descript +=f"得分{self.point}分\n" 
        return  descript
    
   


if __name__ =="__main__":
    
    print("===========擲骰子遊戲開始========")
    c = pyip.inputNum("請問幾位玩家?(最多5位,至少1位)",max=5,min=1)
    p=[]
    score=[]
    i=1
    for i in range(1,c+1):
        p.append(f"玩家{i}")
        p[i-1] = Player(f"玩家{i}")
        score.append(p[i-1].value)
        print(p[i-1])
        
    
    if c > 1:
        i = 0
        win = []
        s =max( [p[i].point for i in range(c)] )
   
        for i in range(c):
            if s==p[i].point :
                win.append(p[i].name)      
        print(f'贏家是:{win}')

    print("遊戲结束")



   

    