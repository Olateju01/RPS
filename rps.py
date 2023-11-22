#the random variable module makes available random values
import random

#created a variable player_choice to take in 3 values from users
player_choice = input(" Enter...\n 1 for Rock \n 2 for Paper or \n 3 for Scissors\n")

#the players choice was converted into  integer(casted)
player = int(player_choice)

#I checked to confirm only number 1,2 and 3 can be inputed
if player < 1 or player > 3:
    print(f"You can only enter 1,2 or 3")
else:
    print(f"You chose {player}")

#I created another variable called computer_choice that is populated by the choice() method
computer_choice = random.choice("123")

#I casted computer_choice into an integer then saved it into a variable called computer
computer = int(computer_choice)
print(f"computer chose {computer}")

#I did my comparison and printed the corresponding messages
if player == 1 and computer== 3:
    print(f"You win!🥳")
elif player ==2 and computer == 1:
    print(f"You win!🥳")
elif player == 3 and computer == 2:
    print(f"You win!🥳")
elif player == computer:
    print(f"It's a tie😒")
else:
    print(f"Computer wins🐍")
