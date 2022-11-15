# key only dict for the Tic-tac-toe
class Game:
    def __init__(self):
      self.game_field = {1:"", 2:"", 3:"", 4:"", 5:"",6:"",7:"",8:"",9:"",}

class Player:
    counter = 1

    def __init__(self):
      self.player_symbol = ""
      self.player_name = self.set_name()
      self.player_symbol = self.set_symbol()
      Player.counter += 1
  
    def set_name(self):
      result = input("Player " + str(Player.counter) + " choose your player name (only alphanumeric): ")  
      while True:
        #Testing if Input okay
        if len(result) == 0:
          result = input("Input cannot be empty. Please enter a string: ")
          continue

        if not result.isalnum():
          #checking input
          result = input("Input cannot be non-alphanumeric. Please enter a string: ")
          continue
        else:
          #Value is okay 
          break  
      return result

    def set_symbol(self):
      result = input(input("Player " + self.player_name + " please enter a single letter as your Symbol: "))
      #Testing if Input okay
      while True:
        if not result.isalpha() or not len(result) == 1:
          #checking input
          result = input("Input cannot be non-alpha or contain more than one character. Please enter a letter: ")
          continue
        else:
          #Value is okay
          break  
      return result

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
