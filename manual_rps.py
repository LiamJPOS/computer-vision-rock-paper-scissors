import random
rps = ['rock', 'paper', 'scissors']

def get_computer_choice():
    return random.choice(rps)

def get_user_choice():
    while True:
        choice = input("Choose rock, paper, or scissors: ")
        choice = choice.lower()
        if choice not in rps:
            print("Please choose rock, paper, or scissors.")
            continue
        else:
            return choice
        
def get_winner(computer_choice, user_choice):
    if user_choice == computer_choice:
        print("It is a tie!")
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        print("You won!")
    else:
        print("You lost")
    
def play():
    computer_choice = get_computer_choice()
    user_choice = get_user_choice()
    get_winner(computer_choice, user_choice)    
    
play()