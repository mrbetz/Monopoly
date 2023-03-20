#Imports + Functions + Lists + Dictionaries START
import random

def nextPart():
  next = input("Press [enter] to continue")
  next = next
  print()

#Dice rolling function
def diceroll():
  dice1 = int(random.randint(1, 6))
  dice2 = int(random.randint(1, 6))
  total_dice = dice1 + dice2
  print("You rolled a " + str(total_dice) + ".")
  print()
  return total_dice

#Resets location
def resetLocation(site):
  playerSpace[index] = site
  location = spaces[site]

def inherit(value):
  playerMoney[currentPlayerName]+=value
  print("Your new balance is: " + str(playerMoney[currentPlayerName]))
  
  
playerSpace = []
playerNames = []
jail = []
bankrupt = []
chanceCards = [
  "Go to PENNSYLVANIA AVENUE. Do not collect $200 if you pass GO.",
  "Advance to the nearest railroad.",
  "The FREE PARKING area needs repair. Go to FREE PARKING and pay $200 to the bank.",
  "JAILBREAK! If anyone, including you, is in jail, they are automatically freed from jail.",
  "Go back three spaces.",
  "You accidentally bought the wrong train ticket! Switch spaces with the player going after you.",
  "If you own less than 5 properties, go to jail.",
  "Go to LUXURY TAX. If you own more than 4 properties, pay $500. Otherwise, take $100 from the bank."
]

communityChestCards = [
  "You won the pie eating contest! As a prize, you earned $200.",
  "How dare you steal that purse. Hand the woman you stole it from $150.",
  "Uh oh! You got stuck in a puddle of mud. A man automatically helps you and takes $200 from you.",
  "GET OUT OF JAIL FREE CARD",
  "Looks like you got in a car crash. You lose $1000.",
  "You won the lottery! Collect $400 from the bank.",
  "It's your lucky day. You found $70 on the ground.",
  "You slipped and dropped $250!"
]

spaces = [
  "GO", "MEDITERRANEAN AVENUE", "COMMUNITY CHEST", "BALTIC AVENUE",
  "INCOME TAX", "READING RAILROAD", "ORIENTAL AVENUE", "CHANCE",
  "VERMONT AVENUE", "CONNECTICUT AVENUE", "PASSING JAIL", "ST. CHARLES PLACE",
  "ELECTRIC COMPANY", "STATES AVENUE", "VIRGINIA AVENUE",
  "PENNSYLVANIA RAILROAD", "ST. JAMES PLACE", "COMMUNITY CHEST",
  "TENNESSEE AVENUE", "NEW YORK AVENUE", "FREE PARKING", "KENTUCKY AVENUE",
  "CHANCE", "INDIANA AVENUE", "ILLINOIS AVENUE", "B&O RAILROAD",
  "ATLANTIC AVENUE", "VENTNOR AVENUE", "WATER WORKS", "MARVIN GARDENS",
  "GO TO JAIL", "PACIFIC AVENUE", "NORTH CAROLINA AVENUE", "COMMUNITY CHEST",
  "PENNSYLVANIA AVENUE", "SHORT LINE", "CHANCE", "PARK PLACE", "LUXURY TAX",
  "BOARDWALK"
]

properties = [
  "MEDITERRANEAN AVENUE", "BALTIC AVENUE", "READING RAILROAD",
  "ORIENTAL AVENUE", "VERMONT AVENUE", "CONNECTICUT AVENUE",
  "ST. CHARLES PLACE", "ELECTRIC COMPANY", "STATES AVENUE", "VIRGINIA AVENUE",
  "PENNSYLVANIA RAILROAD", "ST. JAMES PLACE", "TENNESSEE AVENUE",
  "NEW YORK AVENUE", "KENTUCKY AVENUE", "INDIANA AVENUE", "ILLINOIS AVENUE",
  "B&O RAILROAD", "ATLANTIC AVENUE", "VENTNOR AVENUE", "WATER WORKS",
  "MARVIN GARDENS", "PACIFIC AVENUE", "NORTH CAROLINA AVENUE",
  "PENNSYLVANIA AVENUE", "SHORT LINE", "PARK PLACE", "BOARDWALK", 
]

notProperties = [
  "GO", "COMMUNITY CHEST", "INCOME TAX", "CHANCE", "PASSING JAIL",
  "FREE PARKING", "GO TO JAIL", "LUXURY TAX"
]

prices = {
  "MEDITERRANEAN AVENUE": {
    "price": 60,
    "rent": 2
  },
  "BALTIC AVENUE": {
    "price": 60,
    "rent": 4
  },
  "INCOME TAX": {
    "price": 200,
  },
  "READING RAILROAD": {
    "price": 200,
    "rent": 25
  },
  "ORIENTAL AVENUE": {
    "price": 100,
    "rent": 6
  },
  "VERMONT AVENUE": {
    "price": 100,
    "rent": 6
  },
  "CONNECTICUT AVENUE": {
    "price": 120,
    "rent": 8
  },
  "ST. CHARLES PLACE": {
    "price": 140,
    "rent": 10
  },
  "ELECTRIC COMPANY": {
    "price": 150,
    "rent": 4
  },
  "STATES AVENUE": {
    "price": 140,
    "rent": 10
  },
  "VIRGINIA AVENUE": {
    "price": 160,
    "rent": 12
  },
  "PENNSYLVANIA RAILROAD": {
    "price": 200,
    "rent": 25
  },
  "ST. JAMES PLACE": {
    "price": 180,
    "rent": 14
  },
  "TENNESSEE AVENUE": {
    "price": 180,
    "rent": 14
  },
  "NEW YORK AVENUE": {
    "price": 200,
    "rent": 16
  },
  "KENTUCKY AVENUE": {
    "price": 220,
    "rent": 18
  },
  "INDIANA AVENUE": {
    "price": 220,
    "rent": 18
  },
  "ILLINOIS AVENUE": {
    "price": 240,
    "rent": 20
  },
  "B&O RAILROAD": {
    "price": 200,
    "rent": 25
  },
  "ATLANTIC AVENUE": {
    "price": 260,
    "rent": 22
  },
  "VENTNOR AVENUE": {
    "price": 260,
    "rent": 22
  },
  "WATER WORKS": {
    "price": 150,
    "rent": 4
  },
  "MARVIN GARDENS": {
    "price": 280,
    "rent": 24
  },
  "PACIFIC AVENUE": {
    "price": 300,
    "rent": 26
  },
  "NORTH CAROLINA AVENUE": {
    "price": 300,
    "rent": 26
  },
  "PENNSYLVANIA AVENUE": {
    "price": 320,
    "rent": 28
  },
  "SHORT LINE": {
    "price": 200,
    "rent": 25
  },
  "PARK PLACE": {
    "price": 350,
    "rent": 35
  },
  "LUXURY TAX": {
    "price": 100,
  },
  "BOARDWALK": {
    "price": 400,
    "rent": 50
  }
}

propertyLists = {
  1: [],
  2: [],
  3: [],
  4: [],
  5: [],
  6: [],
  7: [],
  8: []
}

playerMoney = {}
#Imports + Functions + Lists + Dictionaries END

#Introduction START
print("Welcome to Monopoly!")
nextPart()

while True:
  #Asks for the number of players
  playerNumber = input(
    "How many people are playing? Enter a number from 2 to 8: ")
  print()
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
print()
nextPart()

#Selecting names START
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
  # print(playerNames)
  # print(playerSpace)
  # print(playerMoney)
  print()
#Selecting names END
#Introduction END

while len(bankrupt) + 1 != len(playerNames):
  turn = 1

  for i in range(1, playerNum):
    print("Player " + str(turn) + "'s turn")
    print()
    index = turn - 1
    #Dice Roll + Space landed on
    intro = input(playerNames[index] + ", press [enter] to roll the dice.")
    print()
    roll = diceroll()
    #FOR TESTING START
    #roll = 7
    #FOR TESTING END
    playerSpace[index] += roll
    location = spaces[playerSpace[index]]
    #Announces which space the player landed on
    print("You landed on " + location)
    print(playerSpace)
    print()
    nextPart()

    #Delete in the future
    currentPlayerName = playerNames[index]
    currentPlayerMoney = playerMoney[currentPlayerName]
    currentPlayerSpace = playerSpace[index]
    
    print(currentPlayerSpace)
    selected = random.randint(1,8)
    #FOR TESTING
    #selected = 6
    
    #Spaces that are not properties
    #Chance cards
    if location == "CHANCE":
      print(chanceCards[selected-1])
      print()
      
      match selected:
        #ADVANCE TO PENNSYLVANIA AVENUE
        case 1:
          resetLocation(34)
          print(playerSpace)
          print()
          
        #ADVANCE TO THE NEAREST RAILROAD
        case 2:
          if playerSpace[index] == 7:
            resetLocation(5)
            print("You landed on " + location)
          if playerSpace[index] == 22:
            resetLocation(25)
            print("You landed on " + location)
          if playerSpace[index] == 37:
            resetLocation(36)
          print(playerSpace)         
          print()
          
        #GO TO FREE PARKING AND PAY $200
        case 3:
          resetLocation(20)
          print("You landed on " + location)
          inherit(-200)
          print(playerSpace)
          print(playerMoney)
          
        #JAILBREAK  
        case 4:
          print("Jailbreak")
          jail = []
          turn+=1
          continue
          
        #GO BACK THREE SPACES
        case 5:
          playerSpace[index] -= 3
          location = spaces[playerSpace[index]]
          print("You landed on " + location)
          if spaces[playerSpace[index]] in notProperties:
            turn+=1
            continue
          else:
            print()
          
        #SWITCH WITH THE PLAYER GOING AFTER YOU
        case 6:
          print("Index: " + str(index))
          spacesBetween = abs(playerSpace[index] - playerSpace[index+1])
          #If last player of the round
          if turn == playerNum:
            #Ahead of next player
            if playerSpace[index] > playerSpace[0]:
              playerSpace[index] -= spacesBetween
              playerSpace[0] += spacesBetween
            #Behind of next player
            else:
              playerSpace[index] += spacesBetween
              playerSpace[index+1] -= spacesBetween
          else:
            #If any other player but the last player is ahead:
            #Ahead of next player
            if playerSpace[index] > playerSpace[index+1]:
              playerSpace[index] -= spacesBetween
              playerSpace[index+1] += spacesBetween
            #Behind of next player
            else:
              playerSpace[index] += spacesBetween
              playerSpace[index+1] -= spacesBetween
          location = spaces[playerSpace[index]]
          print("You landed on " + location)
          print(playerSpace)
          if spaces[playerSpace[index]] in notProperties:
            turn+=1
            continue
          else:
            print()

        #Less than 5 properties --> Jail
        case 7:
            if len(propertyLists[turn]) < 5:
              resetLocation(10)
              jail.append(currentPlayerName)
              print("You are in jail.")
              print(jail)
              print(playerSpace)
            else:
              print("You have more than 5 properties. You are safe.")
            turn+=1
            continue

        #Luxury Tax, More than 4 properties --> -$500, 4 properties or less --> +$100
        case 8:
          resetLocation(39)
          print(playerSpace)
          if len(propertyLists[turn]) > 4:
            inherit(-500)
            print("You have more than 4 properties. You lost $500.")
            print(playerSpace)
          else:
            inherit(100)
            print("You have less than 5 properties. You do not need to pay the Luxury Tax and have gained $100.")
          turn+=1
          continue
      print()
      
    #Community Chest Cards  
    if location == "COMMUNITY CHEST":
      print(communityChestCards[selected-1])
      match selected:
        case 1:
          inherit(200)
          
        case 2:
          inherit(-150)
          
        case 3:
          inherit(-200)
          
        case 4:
          if currentPlayerName in jail:
            jail.remove(currentPlayerName)
            print("You are now out of jail")
          else:
            #adding Get out of Jail Free card to each player if applicable
            propertyLists[turn].append("Get OUT OF JAIL FREE CARD")
            print("You have gained the GET OUT OF JAIL FREE CARD. The next time you go to jail, you will automatically be freed.")
            print(propertyLists)
            break
            #changing the player balance after each of the community chests
            
        case 5:
          inherit(-1000)
          
        case 6:
          inherit(400)
          
        case 7:
          inherit(70)
          
        case 8:
          inherit(-250)
          
      print()
      turn+=1
      continue
      #putting what happens when you land on each of these non-property spaces
      
    if location == "PASSING JAIL":
      print()
      turn+=1
      continue
      
    if location == "FREE PARKING":
      print()
      turn+=1
      continue
      
    if location == "GO TO JAIL":
      print()
      turn+=1
      continue
      
    if location == "GO":
      print()
      turn+=1
      continue
      
    locationPrice = prices[location]["price"]
    print(locationPrice)
    
    #Tax Space
    if "TAX" in location:
      print("You have lost $" + str(locationPrice))
      playerMoney[currentPlayerName] -= locationPrice
      print("Your current balance is $" + str(playerMoney[currentPlayerName]) + ".")
    else:
      propertyRent = prices[location]["rent"]
      print(propertyRent)
      
    if location in properties:
      #Accessing Nested Dictionary item, obtained code from W3 Schools START
      #Enough money to buy property?
      if currentPlayerMoney >= locationPrice:
        #Accessing Nested Dictionary item, obtained code from W3 Schools END
  
        #Do you want to buy a property? START
        while True:
          print("Do you want to buy " + location + " for $" +
                str(locationPrice) + "? Answer yes or no.")
          buy = input().lower()
          
          if buy == "yes":
            #Deduct money
            print(playerMoney[currentPlayerName])
            playerMoney[currentPlayerName] -= locationPrice
            print("Your current balance is $" + str(playerMoney[currentPlayerName]) + ".")
            #removing the location from the properties list and moving them to the list of what each of the players own
            properties.remove(location)
            propertyLists[turn].append(location)
            print(propertyLists)
            print()
            break
          elif buy == "no":
            #does nothing
            print()
            break
          else:
            #ID10T
            print("You didn't enter yes or no.")
            print()
            #Do you want to buy a property? END
  
      else:
        #if you do not have enough money
        print("You don't have enough money to buy " + location + ".")
    else:
      #Checks if a property is already owned (If already owned, it is removed from the property's list. This if statement makes sure that the space the player is on is a property space.)
      if location not in notProperties:
        
        #Checks for owner of property
        playerIndex = 1
        for i in range(1,playerNumber+1):
          if location in propertyLists[playerIndex]:
            playerMoney[playerNames[playerIndex-1]]+=propertyRent
            break
          else:
            playerIndex+=1
        #You own property
        if spaces[playerSpace[index]] in propertyLists[turn]:
          print("You own " + location)
        #You don't own property and must pay owner
        else:
          print(location + " is already owned by " + playerNames[playerIndex-1] + ".")
          playerMoney[currentPlayerName]-=propertyRent
          print("You lost $" + str(propertyRent) + ".")
          print(playerMoney)
    #Goes to next person's turn
    turn += 1