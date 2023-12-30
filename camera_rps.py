# TODO List
# TODO - Implement game logic and use prediction in place of text input
# TODO - Implement a timer
# TODO - Implement points tracker

#-----
import random
import time
import cv2
from keras.models import load_model
import numpy as np

def get_prediction(resized_frame):
    image_np = np.array(resized_frame)
    normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
    data[0] = normalized_image
    prediction = model.predict(data)
    return prediction

def get_user_choice():
    prediction = get_prediction(resized_frame)
    prediction_index = np.argmax(prediction)
    choice = labels[prediction_index]
    return choice

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

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
    user_choice = get_user_choice()
    print(f"You have chosen {user_choice}.")
    computer_choice = get_computer_choice()
    print(f"The computer has chosen {computer_choice}.")
    get_winner(computer_choice, user_choice)

# Load labels
with open('labels.txt') as f:
    labels = [label.lower() for label in f]
    
# Load pre-trained image recognition model
model = load_model('keras_model.h5')

# Open default webcam channel and set window size (640x480)
cap = cv2.VideoCapture(0) 
cap.set(3, 640)
cap.set(4, 480)

# Coordinates for the user rectangle (224x224)
x1, y1, x2, y2 = 408, 216, 632, 440

# Calculate half-width and half-height
half_width = (x2 - x1) // 2

# Coordinates for the computer rectangle on the left side
new_x1 = 10  # Adjust this value for the desired distance from the left side
new_y1 = y1
new_x2 = new_x1 + half_width * 2
new_y2 = y2

# Create an array to hold image data for prediction
# Shape: (batch_size=1, height=224, width=224, channels=3)
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

# Create count down for the game
countdown_start = 0

while True: 
    ret, frame = cap.read()
    
    # Rectangle for user to play
    cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 255, 255), 2)
    # Rectangle for computer to play
    cv2.rectangle(frame, (new_x1, new_y1), (new_x2, new_y2), (255, 255, 255), 2)
    
    # Extract region of image within user rectangle
    roi = frame[y1:x1, y2:x2]
    img = cv2.cvtColor(roi, cv2.COLOR_BGR2RGB)
    resized_frame = cv2.resize(img, (224, 224), interpolation = cv2.INTER_AREA)
    
    #print(get_user_choice())
    
    # Press s to start game
    if cv2.waitKey(1) & 0xFF == ord('s'):
        countdown_start = int(time.time())
        print("Choose rock, paper, or scissors.")
    if int(time.time()) == countdown_start + 3:
        play() 
        countdown_start = 0
        

    cv2.imshow('frame', frame)
    #cv2.imshow('user img', roi)
    
    # Press q to close the window
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
            
# After the loop release the cap object
cap.release()
# Destroy all the windows
cv2.destroyAllWindows()
