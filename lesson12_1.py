class Person:
    def __init__(self,name:str,weight:int,height:int):
        self.__name = name
        self.weight = weight
        self.height = height
    #property
    @property
    def name(self) -> str:
        return self.__name

    #method
    def bmi(self) -> float:
        return round(self.weight / (self.height / 100) ** 2,ndigits=2)

    def __str__(self) -> str:
        return f"name={self.__name}\nweight={self.weight}\nheight={self.height}"
    

if __name__ == '__main__':
    p1 = Person("robert",78,183)
    #p1.name = "vivan"
    print(p1.name)    
    print(p1.bmi())
