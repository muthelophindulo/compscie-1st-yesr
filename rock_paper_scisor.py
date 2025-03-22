"""
Name: Muthelo Phindulo
Student Number: 225004680

Program Name: Rock_Paper_Scissors game

Input: user enters the move they want to play between 1,2, and 3

output: the program decides whether the computer wins or the user wins
        depending on the move that the computer enter, 
        if they are the same then it is a draw
"""

import random   #to randomly generate the move for the computer

#welcoming message
print('*' * 5 + " ROCK, PAPER, SCISSORS GAME " + '*' * 5)
print()

#the player enters how many times they want to play
plays = int(input("enter how many times you want to play: "))
print()
print('''
To play enter 
      1 for rock
      2 for paper
      3 for scissors
''')
print()
#the scores for both the computer and the player
computer_score = 0
player_score = 0
draws = 0

#create all the possible moves that the player might go for
while plays > 0: #for play in range(plays): #how many times the code should run
    #player MOVE
    player_move = int(input("enter your move here: "))
    print()

    #COMPUTER MOVE
    computer_move = random.randint(1,3)
    #all the possible values that can be played by the computer and player
    if player_move == 1 and computer_move == 2: #if the player goes for rock and the computer goes for paper
        print("player move: ", player_move, "\n", "computer move: ",computer_move, sep="",end="\n")   
        print()       
        print("Paper beats Rock, COMPUTER WINS!!")
        print()
        computer_score += 1
        plays -= 1
    
    elif player_move == 1 and computer_move == 3:
        print("player move: ", player_move, "\n", "computer move: ",computer_move, sep="",end="\n")   
        print()     
        print("Rock beats Scissors, PLAYER WINS!!")
        print()
        player_score += 1
        plays -= 1

    elif player_move == 2 and computer_move == 1: #if the player goes for paper and computer goes for rock 
        print("player move: ", player_move, "\n", "computer move: ",computer_move, sep="",end="\n")   
        print("Paper beats Rock, PLAYER WINS!!")
        print()
        player_score += 1
        plays -= 1

    elif player_move == 2 and computer_move == 3:
        print("player move: ", player_move, "\n", "computer move: ",computer_move, sep="",end="\n")   
        print("scissors beats Paper, COMPUTER WINS!!")
        print()
        computer_score += 1
        plays -= 1
    
    elif player_move == 3 and computer_move == 2:
        print("player move: ", player_move, "\n", "computer move: ",computer_move, sep="",end="\n")   
        print("scissors beats Paper, PLAYER WINS!!")
        print()
        player_score += 1
        plays -= 1

    elif player_move == 3 and computer_move == 1:
        print("player move: ", player_move, "\n", "computer move: ",computer_move, sep="",end="\n")   
        print("rock beats scissors, COMPUTER WINS!!")
        print()
        computer_score += 1
        plays -= 1

    elif player_move == computer_move: #if both computer and player have the same move
        print("player move: ", player_move, "\n", "computer move: ",computer_move, sep="",end="\n")   
        print("It is a draw")
        print()
        plays -= 1
        draws += 1
    else:
        print("move out of range, try again")

print(" the computer has a score of: ",computer_score,"\n","the player has a score of: ", player_score,"\n","number of draws is: ",draws,"\n",end="\n")

if computer_score > player_score:
    print(f"computer won with {computer_score} : {player_score} player")
elif player_score > computer_score:
    print(f"player won with {player_score} : {computer_score} computer")
else:
    print(f"it is a draw of computer {computer_score} : {player_score} player")