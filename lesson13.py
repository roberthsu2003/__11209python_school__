import random
import pyinputplus as pyip

class Player:
   def __init__(self,name:str,dice1:int,dice2:int,dice3:int,dice4:int):
      self.name = name
      self.__dice1 = dice1
      self.__dice2 = dice2
      self.__dice3 = dice3
      self.__dice4 = dice4
   
   def __play(self) -> int:
      
      
      min = 1
      max = 6
      scores=0

      while scores==0:
         dice1 = random.randint(min, max)
         dice2 = random.randint(min, max)
         dice3 = random.randint(min, max)
         dice4 = random.randint(min, max)
         print("++++++++++++++++++++++++++++") 
         print(dice1,dice2,dice3,dice4)

         n1=int(bool(dice1==dice2 and dice1==dice3 and dice1==dice4 and dice2==dice3 and dice2==dice4 and dice3==dice4))
         n2=int(bool(dice1 != dice2 and dice1 != dice3 and dice1!=dice4 and dice2!=dice3 and dice2!=dice4 and dice3!=dice4))

         scores=0

         if n1==1:
            print(f"丟出天王:{dice1},{dice2},{dice3},{dice4}")
            scores=12+dice1
         elif n2==1:
            print(f"骰子都不同:{dice1},{dice2},{dice3},{dice4}->再擲")
            scores=0  #continue
         elif (dice1==dice2) and (dice3==dice4):
            if dice1>dice3:
               scores=dice1+dice2
            else:
               scores=dice3+dice4
         elif (dice2==dice3) and (dice1==dice4):
            if dice1>dice2:
              scores=dice1+dice4
            else:
              scores=dice2+dice3
         elif (dice1==dice3) and (dice2==dice4):
            if dice1>dice2:
               scores=dice1+dice3
            else:
               scores=dice2+dice4
         elif dice1==dice2:
            if dice1==dice3 or dice1==dice4:
               print("骰子3顆相不同->再擲")
               scores=0  #continue
            else:
               scores=dice3+dice4
         elif dice1==dice3:
            if dice1==dice2 or dice1==dice4:
               print("骰子3顆相不同->再擲") 
               scores=0  #continue
            else:
               scores=dice2+dice4
         elif dice1==dice4:
            if dice1==dice2 or dice1==dice3:
              print("骰子3顆相不同->再擲") 
              scores=0  #continue 
            else:
              scores=dice2+dice3
         elif dice2==dice3:
            if dice2==dice1 or dice2==dice4:
               print("骰子3顆相不同->再擲")  
               scores=0  #continue
            else:
               scores=dice1+dice4
         elif dice2==dice4:
            if dice2==dice1 or dice1==dice3:
               print("骰子3顆相不同->再擲") 
               scores=0  #continue 
            else:
               scores=dice1+dice3
         elif dice3==dice4:
            if dice3==dice1 or dice3==dice2:
               print("骰子3顆相不同->再擲")  
               scores=0  #continue
            else:
               scores=dice1+dice2
      if scores > 0:
         print(f"得點:{scores}")

         return scores

   @property
   def dice1(self) -> int:
      return self.__dice1
   @property
   def dice2(self) -> int:
      return self.__dice2
   @property
   def dice3(self) -> int:
      return self.__dice3
   @property
   def dice4(self) -> int:
      return self.__dice4
   @property
   def scores(self) -> int:
      return self.__play()

   def __repr__(self) -> str:
      return  f'name:{self.name}\n,骰子1點數:{self.dice1}\n,骰子2點數:{self.dice2}\n,骰子3點數:{self.dice3}\n,骰子4點數:{self.dice4}\n,得分:{scores}'
	
if __name__ == "__main__":
   p1 = Player("You")
   print(p1.scores)
   print(p1)

   p2 = Player("Boss")
   print(p2.scores)
   print(p2)	