#%%
import cv2
import numpy as np

img = cv2.imread('test3.jpg')

hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
lowerVal = np.array([0,0,0])
upperVal = np.array([10,10,10])  #[blue green red]
mask = cv2.inRange(img,lowerVal,upperVal)


cv2.imshow('hsv',hsv)
cv2.imshow('mask',mask)

cv2.waitKey()
cv2.destroyAllWindows()

# %%
'''
import cv2
import requests
import numpy as np

url = 'http://192.168.43.1:8080/shot.jpg'

while True:
    img_resp = requests.get(url)
    img_arr = np.array(bytearray(img_resp.content), dtype = np.uint8)
    img = cv2.imdecode(img_arr,-1)
    hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    lowerVal = np.array([0,0,0])
    upperVal = np.array([10,10,10])  #[blue green red]
    red_mask = cv2.inRange(hsv,lowerVal,upperVal)
    red = cv2.bitwise_and(hsv,img,mask = red_mask)

    cv2.imshow('cam',hsv)
    

    if cv2.waitKey(1)== 27:
        break
'''

# %%