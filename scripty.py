#Modules
from random import randrange 

# key only dict for the Tic-tac-toe
class Game:
    def __init__(self):
      self.game_field = {1:" ", 2:" ", 3:" ", 4:" ", 5:" ",6:" ",7:" ",8:" ",9:" "}
      self.finished = False
      self.current_player = int()

    def __repr__(self):
      return "A Game of Tic-Tac-Toe!"

    def check_win(self):
      won = False
      if self.game_field[1] == self.game_field[2] and self.game_field[1] == self.game_field[3] and self.game_field[3] != " ":
        won = True
      elif self.game_field[4] == self.game_field[5] and self.game_field[4] == self.game_field[6] and self.game_field[6] != " ":
        won = True
      elif self.game_field[7] == self.game_field[8] and self.game_field[7] == self.game_field[9] and self.game_field[9] != " ":
        won = True
      elif self.game_field[1] == self.game_field[5] and self.game_field[1] == self.game_field[9] and self.game_field[9] != " ":
        won = True
      elif self.game_field[3] == self.game_field[5] and self.game_field[3] == self.game_field[7] and self.game_field[7] != " ":
        won = True
      self.finished = won
      return won

    def print_playing_field(self):
      print("  " + self.game_field[1] + "  |  " + self.game_field[2] + "  |  " + self.game_field[3])
      print("-----------------")
      print("  " + self.game_field[4] + "  |  " + self.game_field[5] + "  |  " + self.game_field[6])
      print("-----------------")
      print("  " + self.game_field[7] + "  |  " + self.game_field[8] + "  |  " + self.game_field[9])
      if Game.check_win(self):
        print("Games ends with one Winner!")
        self.finished = True
        exit()   

    def player_input(self, player):
      self.current_player = player.counter
      result = None
      input_value = input("Player "+ player.player_name + " choose your Field:")
      while result is None:
        if game.game_field[int(input_value)] != " ":
          input_value = input("Player "+ player.player_name + " choose your Field:")
          continue
        else:
          result = input_value
          break
      self.game_field[int(result)] = player.player_symbol
      self.print_playing_field() 

class Player:
    counter = 1

    def __init__(self):
      self.player_name = self.set_name()
      self.player_symbol = self.set_symbol()
      self.counter = Player.counter
      Player.counter += 1

    def __repr__(self):
      return "Player_Name: " + self.player_name + " Player_Symbol:" + self.player_symbol
      return f"<Test player_name:{self.player_name} player_symbol:{self.self.player_symbol}>"
  
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

#Creating player and game instances 
game = Game()
player_one = Player()
player_two = Player()

#Intro
print("The Tic-Tac-Toe Game!")
print("")
print("Who ist goning to play?")
print("")
#playingfield showing fields and numbers
print("")
print("The shown numbers are the Input you have to choose to paint your Symbol into the field ")
print("")
print("  1  |  2  |  3  ")
print("-----------------")
print("  4  |  5  |  6  ")
print("-----------------")
print("  7  |  8  |  9  ")
print("")
print("I am going to randomly select the starting player!")
print("")

#random number in range of counter to determine the starting player. player.counter every game between 1 and 2
first_player = randrange(1, 3, 1)
#second_player = 1 if first_player != 1 else 2
#using the player.counter
if first_player == player_one.counter:
  print(player_one.player_name + " ist the first Player.")
else:
  print(player_two.player_name + " ist the first Player.")
game.current_player = first_player
player = player_one if game.current_player == 1 else player_two

#loop?! questioning for Input for the playingfield
while not game.finished:
  game.player_input(player)
  if player == player_one:
    player = player_two
  else:
    player = player_one