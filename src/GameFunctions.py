from src.Player import Giant , Solider , Support
from .GameVars import GameVariables




def createGame() -> None:
      for i in range(GameVariables.PlayerCount):
        name = input("karakterinize isim veriniz: ")
        team = input("Hangi takımı istersiniz: A-B")

        print("1 - 3 arası karakterinizin türünü seçiniz:\n ")
        species = int(input("1-Giant\n2-Solider\n3-Support:\n "))


        if species == 1:
            player = Giant(name , team)
            GameVariables.Players.append(player)
        elif species == 2:
            player = Solider(name , team)
            GameVariables.Players.append(player)
        else:
            player = Support(name , team)
            GameVariables.Players.append(player)

def startGame():
    pass


