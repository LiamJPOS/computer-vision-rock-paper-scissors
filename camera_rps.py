import time
import random
import cv2
from keras.models import load_model
import numpy as np

def mapper(move_code):    
    class_map = {
    0:'rock',
    1:'paper',
    2:'scissors',
    3:'none'    
    }
    return class_map[move_code]

def get_prediction():
    image_np = np.array(resized_user_frame)
    normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    data[0] = normalized_image
    return model.predict(data, verbose=0)

def get_user_choice():
    prediction_array = get_prediction()
    move_code = np.argmax(prediction_array)
    return mapper(move_code)    

def get_computer_choice ():
    computer_choice = random.choice(["rock", "paper", "scissors"])
    print(f"The computer has chosen {computer_choice}.")
    return computer_choice

def get_winner(computer_choice, user_choice): 
    if user_choice == computer_choice:
        print("It is a tie!")
        
    elif user_choice == "rock":
        if computer_choice == "paper":
            print("You lost")  
        else: 
            print("You Won!")
                  
    elif user_choice == "paper":
        if computer_choice == "scissors":
            print("You lost")     
        else:
            print("You won!")
            
    elif user_choice == "scissors":
        if computer_choice == "rock":
            print("You lost")    
        else: 
            print("You won!")

#TODO Create new countdown method that doesn't interfere with camera input
def countdown(time_sec):
    print("Get ready! Choose Rock, Paper, or Scissors!")
    while time_sec > 0:
        end_time = time.time() + 1
        time_sec -= 1
        print(time_sec)
        while time.time() < end_time:
            pass

model_path = 'C:\\Users\\liamo\\Code\\computer-vision-rock-paper-scissors\\keras_model.h5'
model = load_model(model_path)
rounds_played = 0

#Open webcam in CV
capture = cv2.VideoCapture(0)
while True: 
    ret, frame = capture.read()
    
    #standardize frame size
    frame = cv2.resize(frame, (640, 480), interpolation=cv2.INTER_AREA) #takes (width, height)    
    #user rectangle 
    cv2.rectangle(frame, (10, 240), (214, 470), (255,255,255), thickness=2)
    #computer rectangle 
    cv2.rectangle(frame, (426, 240), (630, 470), (255,255,255), thickness=2)  

    #extract and resize region in user rectangle
    user_frame = frame[244:466, 14:204] #takes [y:y+h,x:x+w]
    resized_user_frame = cv2.resize(user_frame, (224, 224), interpolation = cv2.INTER_AREA)

    #predict user move
    user_choice = get_user_choice()
    print(f'You have chosen {user_choice}')
    
    #get the winner
    if user_choice != 'none':

        computer_choice = get_computer_choice()
        get_winner(computer_choice, user_choice)
        rounds_played += 1

    cv2.imshow('Rock Paper Scissors', frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    if rounds_played == 5:
        break
    
capture.release()
cv2.destroyAllWindows


