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
    user_choice = mapper(move_code)    
    print(f'You have chosen {user_choice}')
    return user_choice

def get_computer_choice ():
    computer_choice = random.choice(["rock", "paper", "scissors"])
    print(f"The computer has chosen {computer_choice}.")
    return computer_choice

def get_winner(computer_choice, user_choice): 
    if user_choice == computer_choice:
        print("It is a tie!")
        return 'tie'
        
    elif user_choice == "rock":
        if computer_choice == "paper":
            print("You lost")  
            return 'computer'
        else: 
            print("You Won!")
            return 'user'

    elif user_choice == "paper":
        if computer_choice == "scissors":
            print("You lost")   
            return 'computer'  
        else:
            print("You won!")
            return 'user'
            
    elif user_choice == "scissors":
        if computer_choice == "rock":
            print("You lost")   
            return 'computer' 
        else: 
            print("You won!")
            return 'user'

model_path = 'C:\\Users\\liamo\\Code\\computer-vision-rock-paper-scissors\\keras_model.h5'
model = load_model(model_path)
rounds_played = 0
user_wins = 0 
computer_wins = 0
countdown = 5
font = cv2.FONT_HERSHEY_SIMPLEX
computer_choice = 'none'
user_choice = 'none'
winner = 'none'

#Open webcam in CV
capture = cv2.VideoCapture(0)
while True:
    
    #Read and display frame 
    ret, frame = capture.read()
    
    #standardize frame size
    frame = cv2.resize(frame, (640, 480), interpolation=cv2.INTER_AREA) #takes (width, height)    
    #user rectangle 
    cv2.rectangle(frame, (10, 240), (214, 470), (255,255,255), thickness=2)
    #display the information
    cv2.putText(frame, 'Let\'s play Rock, Paper, Scissors', (10, 30), font, 1, (255, 255, 255), thickness=2)
    cv2.putText(frame, 'Press Q to start the round', (10, 70), font, 0.7, (255, 255, 255), thickness=2)
    cv2.putText(frame, "Your Move: " + user_choice,
            (30, 370), font, 0.5, (255, 255, 255), 2, cv2.LINE_AA)
    cv2.putText(frame, "Computer's Move: " + computer_choice,
            (410, 370), font, 0.5, (255, 255, 255),2, cv2.LINE_AA)
    cv2.putText(frame, "Winner: " + winner,
            (250, 200), font, 0.7, (0, 0, 255), 2, cv2.LINE_AA)
    cv2.putText(frame, "You: " + str(user_wins),
        (10, 100), font, 0.5, (0, 0, 255), 2, cv2.LINE_AA)
    cv2.putText(frame, "Computer: " + str(computer_wins),
        (10, 120), font, 0.5, (0, 0, 255), 2, cv2.LINE_AA)
            
    cv2.imshow('Rock Paper Scissors', frame)
    
    k = cv2.waitKey(125)
    if k == ord('q'):
        previous_time = time.time()
        
        while countdown >= 0:
            ret, frame = capture.read()
            
            #Display countdown on each frame
            cv2.putText(frame, 'Choose rock, paper, or scissors', (10, 30), font, 1, (255, 255, 255), thickness=2)
            cv2.putText(frame, str(countdown), (300, 200), font, 5, (255, 255, 255), thickness=2)
            #user rectangle 
            cv2.rectangle(frame, (10, 240), (214, 470), (255,255,255), thickness=2)
            
            cv2.imshow('Rock Paper Scissors', frame)
            cv2.waitKey(125)
            
            current_time = time.time()
            
            if current_time - previous_time >= 1:
                previous_time = current_time
                countdown -= 1
        else:
            ret, frame = capture.read()
            
            #extract and resize region in user rectangle
            user_frame = frame[244:466, 14:204] #takes [y:y+h,x:x+w]
            resized_user_frame = cv2.resize(user_frame, (224, 224), interpolation = cv2.INTER_AREA)
            
            #predict user move
            user_choice = get_user_choice()
            
            #get the winner
            if user_choice != 'none':
                computer_choice = get_computer_choice()
                winner = get_winner(computer_choice, user_choice)
                if winner == 'user':
                    user_wins += 1
                if winner == 'computer':
                    computer_wins += 1
                    
                rounds_played += 1
                

            else: 
                computer_choice = 'none'
                print('Choose rock, paper or scissors when the timer reaches 0')
        
        countdown = 5    
        
    #Press esc to close game
    if cv2.waitKey(1) & k == 27:
        break
    if user_wins == 3:
        print('You have won the most rounds! You win!')
        break
        
    if computer_wins == 3:
        print('The computer has won the most rounds. You lost.')
        break
    if rounds_played == 5:
        if user_wins > computer_wins:
            print('You have won the most rounds! You win!')
        elif computer_wins > user_wins:
            print('The computer has won the most rounds. You lost.')
        else:
            print('You both tied. 5 ties in a row is a 0.41\% chance!')
        break
    
capture.release()
cv2.destroyAllWindows
