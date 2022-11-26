# Computer Vision RPS
This project takes an image classification model of the hand positions for the game rock paper scissors, trained using Google's Teachable Machine, that is built on Tensorflow.js (https://github.com/googlecreativelab/teachablemachine-community/), and allows the user to play rock paper scissors with their webcam. The game is coded in Python. 

## Prerequesites
- Python 3.8.*
- USB Webcam
> To input program flow

## Milestone 1
- Environment created.

## Milestone 2
- Trained model with 4 labels "Rock", "Paper", "Scissors", and "Nothing" using 50 images for each class.

- Accuracy of model to be tested. 

- Each class will be used as conditions in the logic of the game.

## Milestone 3
- Librarys installed.

- Model tested. (to input)

## Milestone 4

- Logic of game created with manual input ready for integration with OpenCV input from trained model. First iteration uses if-elif-else statements.

```python

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
            
```
