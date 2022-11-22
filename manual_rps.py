import random
rps = ["Rock", "Paper", "Scissors"]

def get_computer_choice():
    return random.choice(rps)
    
def get_user_choice():
    return random.choice(rps)

user_choice = get_user_choice()
computer_choice = get_computer_choice()

print(user_choice)
print(computer_choice)
