import cv2

cap = cv2.VideoCapture(0) #default webcam channel
cap.set(3, 640)
cap.set(4, 480)

# Coordinates for the user rectangle rectangle (224x224)
x1, y1, x2, y2 = 408, 216, 632, 440

# Calculate half-width and half-height
half_width = (x2 - x1) // 2

# Coordinates for the computer rectangle on the left side
new_x1 = 10  # Adjust this value for the desired distance from the left side
new_y1 = y1
new_x2 = new_x1 + half_width * 2
new_y2 = y2

while True:
    success, img = cap.read()
    
    #User rectangle
    cv2.rectangle(img, (x1, y1), (x2, y2), (255, 255, 255), 2)
    #Computer rectangle
    cv2.rectangle(img, (new_x1, new_y1), (new_x2, new_y2), (255, 255, 255), 2)
    
    
    cv2.imshow("Image", img)
    cv2.waitKey(1) 
    
