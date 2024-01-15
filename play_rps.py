#TODO
#TODO - Rewrite the current game using classes to practise and tidy it up 
#TODO - Add countdown text (create score object or method to draw in Rps?)
#TODO - Add play again option (press c to continue)
#TODO - add icons to Computer_square to show what computer has picked
#TODO - add score text on screen (draw method in Rps?)
#TODO - Create gif of finished game to add to README
#TODO - Update README
#TODO - Tidy up files

import random
import time
import cv2
from keras.models import load_model
import numpy as np

class Screen_square():
    def __init__(self, coordinates):
        self.x1, self.y1, self.x2, self.y2 = coordinates
        
    def draw_square(self, frame):
        cv2.rectangle(frame, (self.x1, self.y1), (self.x2, self.y2), (255, 255, 255), 2)
    
class User_square(Screen_square):
    def __init__(self, model=False):
        self.model = load_model(model)
        self.prediction_array = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    #Returns normalized image array of area in square to an np array usable in keras model
    def convert_image(self, frame):
        extracted_region = frame[self.y1:self.x1, self.y2:self.x2]
        extracted_region = cv2.cvtColor(extracted_region, cv2.COLOR_BGR2RGB)
        extracted_region = cv2.resize(extracted_region, (224, 224), interpolation = cv2.INTER_AREA)
        image_array = np.array(extracted_region)
        normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1 # Normalize the image
        return normalized_image_array
    #Returns model prediction of np array converted from area of image in square
    #rock, paper, scissors, nothing
    def get_user_move(self):
        self.prediction_array[0] = self.convert_image(frame)
        model_prediction = self.model.predict(self.prediction_array)
        prediction_index = np.argmax(model_prediction)
        predicted_move = ['rock', 'paper', 'scissors', 'nothing'][prediction_index]
        return predicted_move

class Computer_square(Screen_square):
    def get_computer_choice(self):
        return random.choice(['rock', 'paper', 'scissors'])
    
    def show_choice_icon(self):
        pass

class Rps():
    def __init__(self):
        self.user_wins = 0
        self.computer_wins = 0
        self.rounds_played = 0
        self.countdown = 0

    #TODO put game logic
    #TODO implement countdown logic here
    def start_round(self):
        pass

cap = cv2.VideoCapture(0)
user_square = User_square(coordinates=[408, 216, 632, 440], model="keras_model.h5")
computer_square = Computer_square(coordinates=[10, 216, 234, 440])

while True:
    success, frame = cap.read()
    user_square.draw_square(frame)
    computer_square.draw_square(frame)
    cv2.imshow('RPS', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

