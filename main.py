#Imports + Functions + Lists + Dictionaries START
import random

def nextPart():
  next = input("Press [enter] to continue")
  next = next
  print()

#Dice rolling function
def diceroll():
  dice1 = int(random.randint(1,6))
  dice2 = int(random.randint(1,6))
  total_dice = dice1 + dice2
  print("You rolled a " + str(total_dice) + ".")  
  print()
  return total_dice
  
playerSpace = []
playerNames = []
spaces = [
  "GO",
  "MEDITERRANEAN AVENUE",
  "COMMUNITY CHEST",
  "BALTIC AVENUE",
  "INCOME TAX",
  "READING RAILROAD",
  "ORIENTAL AVENUE",
  "CHANCE",
  "VERMONT AVENUE",
  "CONNECTICUT AVENUE",
  "PASSING JAIL",
  "ST. CHARLES PLACE",
  "ELECTRIC COMPANY",
  "STATES AVENUE",
  "VIRGINIA AVENUE",
  "PENNSYLVANIA RAILROAD",
  "ST. JAMES PLACE",
  "COMMUNITY CHEST",
  "TENNESSEE AVENUE",
  "NEW YORK AVENUE",
  "FREE PARKING",
  "KENTUCKY AVENUE",
  "CHANCE",
  "INDIANA AVENUE",
  "ILLINOIS AVENUE",
  "B&O RAILROAD",
  "ATLANTIC AVENUE",
  "VENTNOR AVENUE",
  "WATER WORKS",
  "MARVIN GARDENS",
  "GO TO JAIL",
  "PACIFIC AVENUE",
  "NORTH CAROLINA AVENUE",
  "COMMUNITY CHEST",
  "PENNSYLVANIA AVENUE",
  "SHORT LINE",
  "CHANCE",
  "PARK PLACE",
  "LUXURY TAX",
  "BOARDWALK"
]

properties = [
  "MEDITERRANEAN AVENUE",
  "BALTIC AVENUE",
  "READING RAILROAD",
  "ORIENTAL AVENUE",
  "VERMONT AVENUE",
  "CONNECTICUT AVENUE",
  "ST. CHARLES PLACE",
  "ELECTRIC COMPANY",
  "STATES AVENUE",
  "VIRGINIA AVENUE",
  "PENNSYLVANIA RAILROAD",
  "ST. JAMES PLACE",
  "TENNESSEE AVENUE",
  "NEW YORK AVENUE",
  "KENTUCKY AVENUE",
  "INDIANA AVENUE",
  "ILLINOIS AVENUE",
  "B&O RAILROAD",
  "ATLANTIC AVENUE",
  "VENTNOR AVENUE",
  "WATER WORKS",
  "MARVIN GARDENS",
  "PACIFIC AVENUE",
  "NORTH CAROLINA AVENUE",
  "PENNSYLVANIA AVENUE",
  "SHORT LINE",
  "PARK PLACE",
  "LUXURY TAX",
  "BOARDWALK"
]

#Nested Dictionary code obtained from W3Schools START
prices = {
  "MEDITERRANEAN AVENUE": {
    "price" : 60,
  },
  "BALTIC AVENUE": {
    "price" : 60,
  },
  "INCOME TAX": 200,
  "READING RAILROAD": {
    "price" : 200,
  },
  "ORIENTAL AVENUE": {
    "price" : 100,
  },
  "VERMONT AVENUE": {
    "price" : 100,
  },
  "CONNECTICUT AVENUE": {
    "price" : 120,
  },
  "ST. CHARLES PLACE": {
    "price" : 140,
  },
  "ELECTRIC COMPANY": 150,
  "STATES AVENUE": {
    "price" : 140,
  },
  "VIRGINIA AVENUE": {
    "price" : 160,
  },
  "PENNSYLVANIA RAILROAD": {
    "price" : 200,
  },
  "ST. JAMES PLACE": {
    "price" : 180,
  },
  "TENNESSEE AVENUE": {
    "price" : 180,
  },
  "NEW YORK AVENUE": {
    "price" : 200,
  },
  "KENTUCKY AVENUE": {
    "price" : 220,
  },
  "INDIANA AVENUE": {
    "price" : 220,
  },
  "ILLINOIS AVENUE": {
    "price" : 240,
  },
  "B&O RAILROAD": {
    "price" : 200,
  },
  "ATLANTIC AVENUE": {
    "price" : 260,
  },
  "VENTNOR AVENUE": {
  "price" : 260,
  },
  "WATER WORKS" : 150,
  "MARVIN GARDENS": {
  "price" : 280,
  },
  "PACIFIC AVENUE": {
  "price" : 300,
  },
  "NORTH CAROLINA AVENUE": {
  "price" : 300,
  },
  "PENNSYVANIA AVENUE": {
  "price" : 320,
  },
  "SHORT LINE": 200,
  "PARK PLACE": {
  "price" : 350,
  },
  "LUXURY TAX": 100,
  "BOARDWALK": {
    "price" : 400,
  }
}
#Nested Dictionary code obtained from W3Schools END
playerMoney = {}
#Imports + Functions + Lists + Dictionaries END

#Introduction START
print("Welcome to Monopoly!")
nextPart()

while True:
  #Asks for the number of players
  playerNumber = input(
    "How many people are playing? Enter a number from 2 to 8: ")
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
  name = input("What is the name of player " + str(playerNum) + "? ")
  if len(name) == 0:
    print("You need to enter a name that is at least 1 character long.")
    print()
  elif name in playerNames:
    #if there are two people with the same name
    print("That name is already taken.")
    print()
  else:
    #if names are different
    playerSpace.append(0)
    playerNames.append(name)
    playerMoney[name] = 1500
    playerNum += 1
  print(playerNames)
  print(playerSpace)
  print(playerMoney)
print()
#Introduction END

for i in range(1,playerNum):
  #Dice Roll + Space landed on
  turn = 1
  intro = input(playerNames[turn-1] + ", press [enter] to roll the dice.")
  print()
  roll = diceroll()
  site = playerSpace[turn-1]
  site += roll
  location = spaces[site-1]
  print("You landed on " + location)
  print()
  if location in properties:
#Accessing Nested Dictionary item, obtained code from W3 Schools START
    if playerMoney[playerNames[turn-1]] >= prices[location]["price"]:
#Accessing Nested Dictionary item, obtained code from W3 Schools END
      while True:
        print("Do you want to buy " + location + "? Answer yes or no.")
        buy = input().lower()
        if buy == "yes":
          playerMoney-= prices[location]
        elif buy == "no":
          print()
        else:
          print("You didn't enter yes or no.")
          print()
    else:
      print("You don't have enough money to buy " + location + ".")
  turn+=1
#dice to place
for i in range(1,len(playerNames)):
  if roll == 2:
    print("You landed on " + spaces[0])
    playerSpace[0] = playerSpace[0] + roll
  elif roll == 3:
    print("You landed on " + spaces[0])
    playerSpace[0] = playerSpace[0] + roll

#Game START

#Game END