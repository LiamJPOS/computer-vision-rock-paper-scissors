import random
def countdown(time_sec):
    print("Get ready! Choose Rock, Paper, or Scissors!")
    while time_sec > 0:
        end_time = time.time() + 1
        time_sec -= 1
        print(time_sec)
        while time.time() < end_time:
            pass


#Takes list as input
def get_user_choice():
    user_choice = None
    while user_choice not in ["Rock", "Paper", "Scissors"]:
        user_choice = input("Please enter Rock, Paper, or Scissors: ").title()
    print(f"You have chosen {user_choice}.")
    return user_choice

#Takes list as input
def get_computer_choice ():
    computer_choice = random.choice(["Rock", "Paper", "Scissors"])
    print(f"The computer has chosen {computer_choice}.")
    return computer_choice

#if-elif-else statements used for game logic
def get_winner(computer_choice, user_choice): 
       
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
            
def play():
    user_wins = 0
    computer_wins = 0
    for i in range(5):
        
        if user_wins == 3 or computer_wins == 3:
            break
        
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        round_winner = get_winner(computer_choice, user_choice)
        
        if round_winner == "computer":
            computer_wins += 1
        elif round_winner == "user":
            user_wins += 1
        else:
            pass

if __name__ == '__main__':
    play()