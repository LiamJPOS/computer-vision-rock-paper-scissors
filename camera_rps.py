import time
import random
import cv2
from keras.models import load_model
import numpy as np

model = load_model('keras_model.h5')
cap = cv2.VideoCapture(0)
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

def countdown(time_sec):
    print("Get ready! Choose Rock, Paper, or Scissors!")
    while time_sec > 0:
        end_time = time.time() + 1
        time_sec -= 1
        print(time_sec)
        while time.time() < end_time:
            pass
   
def get_user_input():    
    while True: 
        ret, frame = cap.read()
        resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
        image_np = np.array(resized_frame)
        normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
        data[0] = normalized_image
        cv2.imshow('frame', frame)
    
        if cv2.waitKey(5000):
            countdown(5)
            break 
     
    # After the loop release the cap object
    cap.release()
    # Destroy all the windows
    cv2.destroyAllWindows()

def get_prediction(model, data): 
    prediction = model.predict(data)
    print(prediction)
    return prediction

def interpret_prediction(prediction):
    interpreted_prediction = np.argmax(prediction)
    rps = {0: "Rock", 1: "Paper", 2:"Scissors"}
    return rps[interpreted_prediction]

def get_user_choice():
    get_user_input()
    prediction_array = get_prediction(model, data)
    user_choice = interpret_prediction(prediction_array)        
    print(f"You have chosen {user_choice}.")
    return user_choice

def get_computer_choice ():
    computer_choice = random.choice(["Rock", "Paper", "Scissors"])
    print(f"The computer has chosen {computer_choice}.")
    return computer_choice

#if-elif-else statements used for game logic
def get_winner(computer_choice, user_choice): 
       
    if user_choice == computer_choice:
        print("It is a tie!")
        return ("tie")
            
    elif user_choice == "Rock":
        if computer_choice == "Paper":
            print("You lost")  
        else: 
            print("You Won!")
            
        
        
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
        
    overall_winner = {"computer":computer_wins, "user":user_wins}
    if max(overall_winner, key=overall_winner.get) == "computer":
        print("The computer has won the most rounds. You lose")
    else:
        print("You have won the most rounds. You win!")

if __name__ == '__main__':
    play()
    
                        
            

    

