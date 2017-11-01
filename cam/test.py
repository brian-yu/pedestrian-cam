import cv2
cap = cv2.VideoCapture('http://184.80.5.148/mjpg/video.mjpg')

while True:
  ret, frame = cap.read()
  cv2.imshow('Video', frame)

  if cv2.waitKey(1) == 27:
    exit(0)