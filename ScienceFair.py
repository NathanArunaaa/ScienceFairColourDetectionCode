#Programm Writen By Nathan Aruna and Christon Velmahcos 

#-------------------------------Librays------------------------------------
import cv2
import numpy as np
import imutils
from playsound import playsound
import time 



cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)


while True:
     _,frame= cap.read()

     hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

     


    #-------------------------------Red Section Section------------------------------------#
     lower_red = np.array([0,50,120])
     upper_red = np.array([10,255,255])

     mask = cv2.inRange(hsv,lower_red,upper_red)
     

     cnts = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
     cnts = imutils.grab_contours(cnts)

     for c in cnts:
         area = cv2.contourArea(c)
         if area > 5000:


             cv2.drawContours(frame,[c],-1,(0,255,0), 3)
             M = cv2.moments(c)

             cx = int(M["m10"]/ M["m00"])
             cy = int(M["m01"]/ M["m00"])

             cv2.circle(frame,(cx,cy),7,(255,255,255),-1)
             time.sleep(.2)
             playsound('red.wav')
             

     #-------------------------------Green Section------------------------------------------#
     lower_Green = np.array([40,50,50])
     upper_Green = np.array([80,255,255])

     mask = cv2.inRange(hsv,lower_Green,upper_Green)

     cnts = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
     cnts = imutils.grab_contours(cnts)

     for c in cnts:
         area = cv2.contourArea(c)
         if area > 5000:


             cv2.drawContours(frame,[c],-1,(0,255,0), 3)
             print('Green')
             print('-')

             M = cv2.moments(c)

             cx = int(M["m10"]/ M["m00"])
             cy = int(M["m01"]/ M["m00"])

             cv2.circle(frame,(cx,cy),7,(255,255,255),-1)
             time.sleep(.2)
             playsound('Green.wav')
    
    #-------------------------------Blue Section------------------------------------------#

     lower_Blue = np.array([100,150,0])
     upper_Blue = np.array([140,255,255])

     mask = cv2.inRange(hsv,lower_Blue,upper_Blue)
     

     cnts = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
     cnts = imutils.grab_contours(cnts)

     for c in cnts:
         area = cv2.contourArea(c)
         if area > 5000:


             cv2.drawContours(frame,[c],-1,(0,255,0), 3)
             M = cv2.moments(c)

             cx = int(M["m10"]/ M["m00"])
             cy = int(M["m01"]/ M["m00"])

             cv2.circle(frame,(cx,cy),7,(255,255,255),-1)
             time.sleep(.2)
             playsound('Blue.wav')
    #-------------------------------------------------------------------------------------#        
    


     cv2.imshow("result",frame)

     k = cv2.waitKey(5)
     if k == 27:
         break

cap.release()
cv2.destroyAllWindows()