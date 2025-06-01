import random

print('Welcome to the Coin Guessing Game!')


while True:
    method = input('Choose a method to toss the coin:\n1. Using random.random\n2. Using random.randint\nEnter your choice (1 or 2): ')
    if method in ['1', '2']:
        break
    else:
        print("Invalid choice! Please enter 1 or 2.")

while True:
    guess = input('Enter your guess (head or tail): ').lower()
    if guess not in ['head', 'tail']:
        print("Invalid guess! You must enter 'head' or 'tail'.")
        continue

    if method == '1':
        the_ai_choice = 'head' if random.random() <= 0.5 else 'tail'
    else:
        the_ai_choice = 'head' if random.randint(0, 1) == 0 else 'tail'

    if guess == the_ai_choice:
        print('You won!')
    else:
        print(f'You lost, it was {the_ai_choice}')

    again = input('\nDo you want to play again? (yes/no): ').lower()
    if again != 'yes':
        print('Thanks for playing! See you next time 👋')
        break
