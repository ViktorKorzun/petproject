import random

def get_user_input(prompt):
    while True:
        try:
            user_input = int(input(prompt))
            if user_input < 0:
                print("Please enter a non-negative number.")
                continue
            return user_input
        except ValueError:
            print("Invalid input. Please enter an integer.")

game = True
lifes = 7
computer_number = random.randint(0, 100)
user_number = get_user_input("What number is hidden by computer?: ")

while game:
    lifes -= 1
    if lifes != 0:        
        if user_number < computer_number:
            print(f"You have {lifes} lifes remaining")
            user_number = get_user_input('Your number is lower than the computer number. What\'s next?: ')
        elif user_number > computer_number:
            print(f"You have {lifes} lifes remaining")
            user_number = get_user_input('Your number is higher than the computer number. What\'s next?: ')
        else:
            print(f"You win! Computer number was {computer_number}")
            game = False
    else:
        print('You lose. 0 lifes remaining.')
        lifes -= 1
        game = False