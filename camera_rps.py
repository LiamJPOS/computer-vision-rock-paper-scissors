import random
import cv2
from keras.models import load_model
import numpy as np

model = load_model('keras_model.h5')
cap = cv2.VideoCapture(0)
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

while True: 
    ret, frame = cap.read()
    resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
    image_np = np.array(resized_frame)
    normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
    data[0] = normalized_image
    cv2.imshow('frame', frame)
    # Press q to close the window
    #print(prediction)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break 
# After the loop release the cap object
cap.release()
# Destroy all the windows
cv2.destroyAllWindows()

def get_prediction(model, data): 
    prediction = model.predict(data)
    #return np.argmax(prediction)
    print(prediction)
    return prediction
    
user_choice = np.argmax(get_prediction(model, data))
rps = {0: "Rock", 1: "Paper", 2:"Scissors"}
print(rps[user_choice])
'''
def get_user_choice():
    
    user_choice = None
    while user_choice not in ["Rock", "Paper", "Scissors"]:
        user_choice = rps[np.argmax(get_prediction)]
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
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    get_winner(computer_choice, user_choice)

if __name__ == '__main__':
    play()
'''    