import cv2
import numpy as np 
image= cv2.imread("solar-system.jpg")

cv2.putText(image , "Sun" ,(3 , 250) , cv2.FONT_HERSHEY_COMPLEX , 1.5 , color=(255,255,255))
cv2.putText(image , "Mercury" ,(120 , 245) , cv2.FONT_HERSHEY_COMPLEX , 0.4 , color=(255,255,255))
cv2.putText(image , "Venus" ,(190 , 177) , cv2.FONT_HERSHEY_COMPLEX , 0.5 , color=(255,255,255))
cv2.putText(image , "Earth" ,(288 , 265) , cv2.FONT_HERSHEY_COMPLEX , 0.5 , color=(255,255,255))
cv2.putText(image , "Mars" ,(383 , 260) , cv2.FONT_HERSHEY_COMPLEX , 0.5 , color=(255,255,255))
cv2.putText(image , "Jupitar" ,(570 , 388) , cv2.FONT_HERSHEY_COMPLEX , 0.8 , color=(255,255,255))
cv2.putText(image , "Saturn" ,(770 , 320) , cv2.FONT_HERSHEY_COMPLEX , 0.8 , color=(255,255,255))
cv2.putText(image , "Uranus" ,(970 , 300) , cv2.FONT_HERSHEY_COMPLEX , 0.5 , color=(255,255,255))
cv2.putText(image , "Neptune" ,(1115 , 290) , cv2.FONT_HERSHEY_COMPLEX , 0.5 , color=(255,255,255))



cv2.imshow("Solar-System" , image)

cv2.waitKey(0)