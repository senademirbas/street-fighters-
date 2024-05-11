import random

class BasePlayer:
    hp = 100
    power = 10
    level = 1

    def __init__(self , name:str , team:str):
        self.name = name
        self.team = team

    def attack(self , obj)-> None:
        if obj.team != self.team:
            damage = self.critical()
            obj.hp -= damage 
            print(f"{self.name} attacked {obj.name} and dealt {damage} damage. ")

    def immortal(self):
         return self.hp > 0

    def critical(self) -> float:
         critical_rate = self.power * random.randint(1,3)
         return critical_rate
     

class Giant(BasePlayer):    #Giant inherits from baseplayer
        hp = 1000
        power = 30


class Support(BasePlayer):
    power = 5
    healing_power = 10

    def healing(self , obj):
         obj.hp += self.healing_power * self.level

    def selfHeal(self):
         self.hp += self.healing_power * self.level

class Soldier(BasePlayer): #Soldier
     hp = 300
     power = 30
         
     

