import random

player_choice = input(" Enter...\n 1 for Rock \n 2 for Paper or \n 3 for Scissors\n")
player = int(player_choice)
if player < 1 or player > 3:
    print(f"You can only enter 1,2 or 3")
else:
    print(f"You chose {player}")

computer_choice = random.choice("123")
computer = int(computer_choice)
print(f"computer chose {computer}")

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
