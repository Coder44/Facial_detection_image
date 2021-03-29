import cv2
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
img = cv2.imread('test.jpg')
gray_scale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
face_detect = face_cascade.detectMultiScale(gray_scale, 1.7, 4)
for (x, y, w, h) in face_detect:
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
cv2.imshow('img', img)
cv2.waitKey()