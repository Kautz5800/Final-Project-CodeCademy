# key only dict for the Tic-tac-toe
class Game():
    def __init(self)__:
        game_field = {1:"", 2:"", 3:"", 4:"", 5:"",6:"",7:"",8:"",9:"",}

class Player:
    counter = 1

    def __init__(self):
      self.player_symbol = ""
      self.player_name = input("Player " + str(Player.counter) + " choose your player name:")
      self.player_symbol = input("Player " +self.player_name+" choose your Symbol: ")
      Player.counter += 1


player_one = Player()
player_two = Player()

print("")
print("Player1")
print(player_one.player_name)
print(player_one.player_symbol)
print("")
print("Player2")
print(player_two.player_name)
print(player_two.player_symbol)
