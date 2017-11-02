import cv2
import time
import subprocess
import os



start = time.time()
cap = cv2.VideoCapture('http://24.103.196.243/cgi-bin/viewer/video.jpg?r=1509388702')

ret, frame = cap.read()

print(cap.read())

frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB);
cv2.imwrite('cam.png', frame)
cmd = "./darknet detector test cfg/coco.data cfg/yolo.2.0.cfg yolo.2.0.weights cam.png"# -thresh .2"
#output = subprocess.check_output(cmd.split(), stdout=open(os.devnull, 'w'))

output = subprocess.check_output(cmd.split())

output = output.decode("utf-8").split("\n")

numPeople = len([i.split(":")[0] for i in output if i.split(":")[0] == 'person'])
print(output[0])
print("{} - {} people detected.".format(time.strftime("%d %b %Y %H:%M:%S", time.localtime()), numPeople))
