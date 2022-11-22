import random
rps = ["Rock", "Paper", "Scissors"]
#Takes list as input
def get_user_choice():
    user_choice = None
    while user_choice not in rps:
        user_choice = input("Please enter Rock, Paper, or Scissors: ").title()
    print(f"You have chosen {user_choice}.")
    return user_choice

#Takes list as input
def get_computer_choice ():
    computer_choice = random.choice(rps)
    print(f"The computer has chosen {computer_choice}.")
    return computer_choice

#if-elif-else statements used for game logic
def get_winner(user_choice, computer_choice): 
       
    if user_choice == computer_choice:
        print("It is a tie!")
            
    elif user_choice == "Rock":
        if computer_choice == "Paper":
            print("You lost")
        else: print("You Won!")
        
    elif user_choice == "Paper":
        if computer_choice == "Scissors":
            print("You lost")
        else:
            print("You won!")
            
    elif user_choice == "Scissors":
        if computer_choice == "Rock":
            print("You lost")
        else: 
            print("You won!")

if __name__ == '__main__':
    user_choice = get_user_choice(rps)
    computer_choice = get_computer_choice(rps)
    get_winner(user_choice, computer_choice)