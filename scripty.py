#Modules
from random import randrange 

# key only dict for the Tic-tac-toe
class Game:
    def __init__(self):
      self.game_field = {1:" ", 2:" ", 3:" ", 4:" ", 5:" ",6:" ",7:" ",8:" ",9:" "}

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
      return won

    def print_playing_field(self):
      print("  " + self.game_field[1] + "  |  " + self.game_field[2] + "  |  " + self.game_field[3])
      print("-----------------")
      print("  " + self.game_field[4] + "  |  " + self.game_field[5] + "  |  " + self.game_field[6])
      print("-----------------")
      print("  " + self.game_field[7] + "  |  " + self.game_field[8] + "  |  " + self.game_field[9])
      if Game.check_win(self):
        print("Games ends with one Winner!")
        exit()

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

game = Game()
#Intro

print("The Tic-Tac-Toe Game!")
print("")
print("Who ist goning to play?")
print("")
#Creating player instances 
player_one = Player()
player_two = Player()
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
second_player = 1 if first_player != 1 else 2
#using the player.counter
if first_player == player_one.counter:
  print(player_one.player_name + " ist the first Player.")
else:
  print(player_two.player_name + " ist the first Player.")

if first_player == 1:

  field1 = input("Player "+ player_one.player_name + " choose your Field:")
  game.game_field[int(field1)] = player_one.player_symbol
  game.print_playing_field()

  field2 = input("Player "+ player_two.player_name + " choose your Field:")
  game.game_field[int(field2)] = player_two.player_symbol
  game.print_playing_field()

  field3 = input("Player "+ player_one.player_name + " choose your Field:")
  game.game_field[int(field3)] = player_one.player_symbol
  game.print_playing_field()

  field4 = input("Player "+ player_two.player_name + " choose your Field:")
  game.game_field[int(field4)] = player_two.player_symbol
  game.print_playing_field()

  field5 = input("Player "+ player_one.player_name + " choose your Field:")
  game.game_field[int(field5)] = player_one.player_symbol
  game.print_playing_field()

  field6 = input("Player "+ player_two.player_name + " choose your Field:")
  game.game_field[int(field6)] = player_two.player_symbol
  game.print_playing_field()

  field7 = input("Player "+ player_one.player_name + " choose your Field:")
  game.game_field[int(field7)] = player_one.player_symbol
  game.print_playing_field()

  field8 = input("Player "+ player_two.player_name + " choose your Field:")
  game.game_field[int(field8)] = player_two.player_symbol
  game.print_playing_field()
  
  field9 = input("Player "+ player_one.player_name + " choose your Field:")
  game.game_field[int(field9)] = player_one.player_symbol
  game.print_playing_field()
else:
 
  field1 = input("Player "+ player_two.player_name + " choose your Field:")
  game.game_field[int(field1)] = player_two.player_symbol
  game.print_playing_field()

  field2 = input("Player "+ player_one.player_name + " choose your Field:")
  game.game_field[int(field2)] = player_one.player_symbol
  game.print_playing_field()

  field3 = input("Player "+ player_two.player_name + " choose your Field:")
  game.game_field[int(field3)] = player_two.player_symbol
  game.print_playing_field()

  field4 = input("Player "+ player_one.player_name + " choose your Field:")
  game.game_field[int(field4)] = player_one.player_symbol
  game.print_playing_field()

  field5 = input("Player "+ player_two.player_name + " choose your Field:")
  game.game_field[int(field5)] = player_two.player_symbol
  game.print_playing_field()

  field6 = input("Player "+ player_one.player_name + " choose your Field:")
  game.game_field[int(field6)] = player_one.player_symbol
  game.print_playing_field()

  field7 = input("Player "+ player_two.player_name + " choose your Field:")
  game.game_field[int(field7)] = player_two.player_symbol
  game.print_playing_field()

  field8 = input("Player "+ player_one.player_name + " choose your Field:")
  game.game_field[int(field8)] = player_one.player_symbol
  game.print_playing_field()
  
  field9 = input("Player "+ player_two.player_name + " choose your Field:")
  game.game_field[int(field9)] = player_two.player_symbol
  game.print_playing_field() 


