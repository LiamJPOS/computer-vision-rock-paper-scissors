# Computer Vision Rock Paper Scissors
This project takes an image classification model of the hand positions for the game rock paper scissors, trained using Google's Teachable Machine, that is built on Tensorflow.js (https://github.com/googlecreativelab/teachablemachine-community/), and allows the user to play rock paper scissors with their webcam. The game is coded in Python. 

![Example GIF](https://public.am.files.1drv.com/y4mSdJUdP7TLOmjkPKqD7wQIAkFpTFpDbc2qtk6I1Ysn94cc4O1qe5olDVvLSoV_MuRqm-2jh7eSKHE758jgNxSn5XI6LY9m-POJOEEmczFCvJkm4q8wj64zZ2g5HaBzuGQUiSDzCYXxlruphF3D6SbaLzvXSF-HgOeyoH-emDmTCEg5xx1fQCsSzwLWlOvFcC2FcmBdo-5u7xyAMCyTzY5hIDE8x8zlr9-NQnSNV-PnN4)

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
## Milestone 5
- Added game information text overlay of the frames captured by the webcam using cv2.putText() method. 
- Added variables to track user wins, computer wins, and rounds played. The game currently ends after a hard coded 3 user wins, 3 computer wins, or 5 rounds played. Future improvement would allow user to select these parameters.
```python
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
```
- Added functionality to allow user to start each round with a key press
- Added a timer functionality that captures user input after 5 seconds. 
```python 
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
```
- User input now read by previously trained Tensorflow model

```python 
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
```
- Game completed and playable as minimum viable product. Project completed as set by AiCore, but code improvements to follow.
