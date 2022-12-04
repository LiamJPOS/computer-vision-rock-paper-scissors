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

def get_user_choice():

    resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
    image_np = np.array(resized_frame)
    normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
    data[0] = normalized_image
    prediction = model.predict(data)
    choice_code = np.argmax(prediction)
    user_choice = mapper(choice_code)
    return user_choice
    
def get_computer_choice ():
    computer_choice = random.choice(["Rock", "Paper", "Scissors"])
    print(f"The computer has chosen {computer_choice}.")
    return computer_choice

def get_winner(computer_choice, user_choice): 

    if user_choice == computer_choice:
        print("It is a tie!")
        
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
            
model = load_model('keras_model.h5')
cap = cv2.VideoCapture(0)
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

previous_choice = None
#Game takes place in this loop
while True: 
    ret, frame = cap.read()
    
    user_choice = get_user_choice()
    
    if previous_choice != user_choice:
        if user_choice != 'none':
            computer_choice = get_computer_choice()
            get_winner(computer_choice, user_choice)
        else:
            computer_choice = 'none'
            print('Waiting for user')    
    previous_choice = user_choice
    
    cv2.imshow('frame', frame)
    # Press q to close the window
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break