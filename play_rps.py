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

class Rps():
    def __init__(self):
        self.user_wins = 0
        self.computer_wins = 0
        self.rounds_played = 0
        self.countdown = 0

class Screen_square():
    def __init__(self, coordinates):
        self.x1, self.y1, self.x2, self.y2 = coordinates
        
    def draw_square(self, frame):
        cv2.rectangle(frame, (self.x1, self.y1), (self.x2, self.y2), (255, 255, 255), 2)
    
class User_square(Screen_square):
    def __init__(self, model=False):
        self.model = model
    #Convert image in square to an np array
    def convert_image(self):
        pass
    #Return model prediction of np array converted from image in square
    #rock, paper, scissors, nothing
    def get_predicted_move(self):
        pass

class Computer_square(Screen_square):
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

