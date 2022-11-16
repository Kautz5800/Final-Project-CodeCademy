# key only dict for the Tic-tac-toe
class Game:
    def __init__(self):
      self.game_field = {1:"", 2:"", 3:"", 4:"", 5:"",6:"",7:"",8:"",9:""}

class Player:
    counter = 1

    def __init__(self):
      self.player_symbol = ""
      self.player_name = self.set_name()
      self.player_symbol = self.set_symbol()
      self.counter = Player.counter
      Player.counter += 1
  
    def set_name(self):
      result = None  
      input_value = input("Player " + str(Player.counter) + " choose your player name (only alphanumeric): ")  
      while result is None:
        input_value = self.check_player_name(self.counter, input_value) 
        #Testing if Input okay
        if len(input_value) == 0:
          input_value = input("Input cannot be empty or be non-alphanumeric. Please enter a string: ")
          continue
        else:
          #Value is okay
          result = input_value 
          break  
      return result

    def set_symbol(self):
      result = None
      input_value = input(self.player_name + " please enter a single letter as your Symbol: ")
      while result is None:
        input_value = self.check_player_symbol(self.counter, input_value)
      #Testing if Input okay
        if len(input_value) != 1 or not input_value.isalpha():
          input_value = input("Input cannot be non-alpha or contain more than one character. Please enter a single letter: ")
          continue
        else:
          #Value is okay
          result = input_value
          break  
      return result
    
    def check_player_name(self, counter, name):
      result = name
      if Player.counter > 1:
        while result == player_one.player_name:
          result = input("Player " + str(Player.counter) + " the choosen name is already in use!. Try again: ")
      return result

    def check_player_symbol(self, counter, symbol):
      result = symbol
      if Player.counter > 1:
        while result == player_one.player_symbol:
          result = input("Player " + str(Player.counter) + " the choosen symbol is already in use!. Try again: ")
      return result
    
#Intro
print("The Tic-Tac-Toe Game!")
print("")
print("Who ist goning to play?")
print("")
#Creating player intances 
player_one = Player()
player_two = Player()
#playingfield
print("")
print("The shown numbers are the Input you have to choose to paint your Symbol into the field ")
print("")
print("  1  |  2  |  3  ")
print("-----------------")
print("  4  |  5  |  6  ")
print("-----------------")
print("  7  |  8  |  9  ")





"""
print("")
print("Player1")
print(player_one.player_name)
print(player_one.player_symbol)
print(player_one.counter)
print("")
print("Player2")
print(player_two.player_name)
print(player_two.player_symbol)
print(player_two.counter)
"""