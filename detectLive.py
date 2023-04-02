import cv2

img=cv2.imread('hi.jpg')
grey=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

faceCascade=cv2.CascadeClassifier('haarcascade_fullbody.xml')
faces=faceCascade.detectMultiScale(grey)
#print(faces)

for(x,y,w,h)in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
    
cv2.imshow('image',img)
cv2.waitKey(0)