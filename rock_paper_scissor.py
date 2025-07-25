import random

emojies = { 'r': '🪨', 's': '✂️', 'p': '📃' }
choices = ['r', 'p', 's']

while True:
    user_choice = input('Rock, Paper or Scissors? (r/p/s): ').lower()
    if user_choice not in choices:
        print('Invalid choice!')
        continue

    machine_choice = random.choice(choices)

    print(f'Your Chose: {emojies[user_choice]}')
    print(f'Computer Chose: {emojies[machine_choice]}')

    if user_choice == machine_choice:
        print('Tie!')
    elif (
        (user_choice == 'r' and machine_choice == 's') or 
        (user_choice == 's' and machine_choice == 'p') or 
        (user_choice == 'p' and machine_choice == 'r')):
        print('You Win!')
    else:
        print('You lose!')

    should_continue = input('Continue? (y/n): ').lower()
    if should_continue == 'n':
        break