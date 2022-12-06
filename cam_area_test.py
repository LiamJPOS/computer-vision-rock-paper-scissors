import cv2 as cv


#returns tuple of (height, width, channels). example (480, 640, 3)
def get_dimensions(img):
    return img.shape

capture = cv.VideoCapture(0)
while True: 
    ret, frame = capture.read()
    #standardize frame size
    frame = cv.resize(frame, (640, 480), interpolation=cv.INTER_AREA) #takes (width, height)    
    #user rectangle based on standardized frame
    cv.rectangle(frame, (10, 240), (214, 470), (255,255,255), thickness=2)
    
    #cropped frame for model to read image in user rectangle
    cropped_frame = frame[244:466, 14:204] #takes [y:y+h,x:x+w]
    
    cv.imshow('frame', frame)
    cv.imshow('cropped frame', cropped_frame)
        
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
    
capture.release()
cv.destroyAllWindows



#default from my cam so just resize to 600, 400, 3 (480, 640, 3)
