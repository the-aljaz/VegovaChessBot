import cv2
import math
import numpy as np


def get_fen_from_pic():
     
    cap = cv2.VideoCapture(1) 
    

    x = 25
    y = 32
    counter = 1
    modra = 3

    kernel = np.ones((5, 5), np.uint8)   
        
    ret, frame = cap.read() 
    frame = frame[0:480, 130:510]

    fen_array = ["0" for x in range(64)]
    for coord in range(64):     
            
        for i in range(10):    

            cv2.circle(frame, (x+i, y+i), 2, [0, modra, 255], 2)

        
        x += 44
        if counter % 8==0:
            counter = 0
            x = 35
            y += 56
            
        counter += 1
        modra += 3
    return frame
    

while True:   
    cv2.imshow("a", get_fen_from_pic())
    cv2.waitKey(1)
  
