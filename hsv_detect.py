import cv2
import requests
import numpy as np

url = 'http://192.168.43.1:8080/shot.jpg'

while True:
    img_resp = requests.get(url)
    img_arr = np.array(bytearray(img_resp.content), dtype = np.uint8)
    img = cv2.imdecode(img_arr,-1)
    hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

    

    cv2.imshow('cam',hsv)
    

    if cv2.waitKey(1)== 27:
        break