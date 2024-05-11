from src.Player import Giant , Soldier , Support
from src.GameVars import GameVariables

def battle(Player1, Player2) -> None:
    while Player1.immortal() and Player2.immortal():
        
        Player1.attack(Player2)
        if Player2.immortal():
            Player2.attack(Player1)

    if Player1.immortal() and Player2.immortal():
        print("It's a draw!!")
    elif Player1.immortal():
        print(f"{Player1.name} wins!!")
    else:
        print(f"{Player2.name} wins!!")

def createGame() -> None:
      for i in range(GameVariables.PlayerCount):
        name = input("Name your character: ")
        team = input("Which team A or B? : ")
    
        print("Choose the character type :\n ")
        species = int(input("1-Giant\n2-Soldier\n3-Support:\n "))


        if species == 1:
            player = Giant(name , team)
            GameVariables.Players.append(player)
        elif species == 2:
            player = Soldier(name , team)
            GameVariables.Players.append(player)
        else:
            player = Support(name , team)
            GameVariables.Players.append(player)

def startGame() -> None:
    print("Fight starts!! Behold the mighty fighters!!\n ")
    Player1 = GameVariables.Players[0]
    Player2 = GameVariables.Players[1]
    print(f"!!!{Player1.name} vs {Player2.name}!!!")
    battle(Player1, Player2)

    pass


