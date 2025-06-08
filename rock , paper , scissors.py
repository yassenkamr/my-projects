import random

options = ['rock', 'paper', 'scissors']

print('Welcome to Rock, Paper, Scissors Game!')

x = input("Press Enter to continue or type 'help' for the rules: ").lower()

if x == 'help':
    print('\n********** RULES **********')
    print('1- You choose and the computer chooses.')
    print('2- Rock smashes scissors = rock wins.')
    print('3- Scissors cut paper = scissors win.')
    print('4- Paper covers rock = paper wins.')
    
    while True:
        player_choice = input("\nEnter your choice (rock, paper, scissors) or type 'exit' to quit: ").lower()

        if player_choice == 'exit' or player_choice == 'quit':
            print("Thanks for playing, see you next time! 👋")
            break

        if player_choice in options:
            ai_choice = random.choice(options)
            print(f"You chose {player_choice}, computer chose {ai_choice}!")

            if player_choice == ai_choice:
                print("It's a tie!")
            elif (player_choice == 'rock' and ai_choice == 'scissors') or \
                 (player_choice == 'scissors' and ai_choice == 'paper') or \
                 (player_choice == 'paper' and ai_choice == 'rock'):
                print("You win! 🎉")
            else:
                print("You lost! 😢")
        else:
            print("Invalid choice. Please enter rock, paper, or scissors.")


elif x == '':
    while True:
        player_choice = input("\nEnter your choice (rock, paper, scissors) or type 'exit' to quit: ").lower()

        if player_choice == 'exit' or player_choice == 'quit':
            print("Thanks for playing, see you next time! 👋")
            break

        if player_choice in options:
            ai_choice = random.choice(options)
            print(f"You chose {player_choice}, computer chose {ai_choice}!")

            if player_choice == ai_choice:
                print("It's a tie!")
            elif (player_choice == 'rock' and ai_choice == 'scissors') or \
                 (player_choice == 'scissors' and ai_choice == 'paper') or \
                 (player_choice == 'paper' and ai_choice == 'rock'):
                print("You win! 🎉")
            else:
                print("You lost! 😢")
        else:
            print("Invalid choice. Please enter rock, paper, or scissors.")

else:
    print("Please press Enter or type 'help'. Nothing else.")
