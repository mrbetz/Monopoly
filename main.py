import random

def nextPart():
  next = input("Press [enter] to continue")
  print()

playerNames = []

print("Welcome to Monopoly!")
nextPart()

while True:
  #Asks for the number of players
  playerNumber = input("How many people are playing? Enter a number from 2 to 8: ")
  try:
    playerNumber = int(playerNumber)
    #playerNumber is out of range
    if playerNumber < 2 or playerNumber > 8:
      print("You did not enter a number from 2 to 8.")
      print()
      continue
    break
  except ValueError:
    #User does not enter an integer
    print("You did not enter a number from 2 to 8.")
    print()

print("There are currently " + str(playerNumber) + " players.")
nextPart()

playerNum = 1
#repeat amount of times corresponding to user input
while len(playerNames) != playerNumber:
  #test
  # print(len(playerNames))
  # print(playerNumber)
  #ask for input
  playerName = input("What is the name of player " + str(playerNum) + "? ")
  if len(playerNum) == 0:
    print("You need to enter a name that is at least 1 character long.")
    print()
  elif playerName in playerNames:
    #if there are two people with the same name
    print("That name is already taken.")
    print()
  else:
    #if names are different
    playerNames.append(playerName)
    playerNum = playerNum + 1
  print(playerNames)