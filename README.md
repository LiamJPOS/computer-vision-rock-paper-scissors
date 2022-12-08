# Computer Vision RPS
This project takes an image classification model of the hand positions for the game rock paper scissors, trained using Google's Teachable Machine, that is built on Tensorflow.js (https://github.com/googlecreativelab/teachablemachine-community/), and allows the user to play rock paper scissors with their webcam. The game is coded in Python. 

## Prerequesites
- Python 3.8.*
- USB Webcam
> To input program flow

## Milestone 1
- Environment created.

## Milestone 2
- Trained model with 4 labels "Rock", "Paper", "Scissors", and "None" using 200 images for each class. Exported Tensorflow .h5 model and text file with labels saved with project

- Images collected with a Python script utilising Opencv-Python. Teachable Machine resizes images to 244x244px so training data small enough to be kept with project files on GitHub. 
 

Examples of training images:

| Rock | Paper | Scissors | None |
|------|:-----:|:---------:|-----|
![Rock](https://github.com/LiamJPOS/computer-vision-rock-paper-scissors/blob/main/image_data/rock/1.jpg?raw=true) | ![Paper](https://github.com/LiamJPOS/computer-vision-rock-paper-scissors/blob/main/image_data/paper/1.jpg?raw=true) | ![Scissors](https://github.com/LiamJPOS/computer-vision-rock-paper-scissors/blob/main/image_data/scissors/1.jpg?raw=true) | ![None](https://github.com/LiamJPOS/computer-vision-rock-paper-scissors/blob/main/image_data/none/1.jpg?raw=true)  
 
 
Each class will be used as conditions in the logic of the game.

## Milestone 3
- Librarys installed.

- Model tested and accruacy improved to over 99% when using only region of the webcam frame as input as shown in examples.


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
