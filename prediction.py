import cv2
import time
import subprocess
import sys

while True:
    try:
        last = time.time()

        cap = cv2.VideoCapture('http://84.35.225.233:83/SnapshotJPEG?Resolution=640x480&amp;amp;Quality=Clarity&amp;amp;1509566566')

        ret, frame = cap.read()

        # Convert to RGB
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB);
        
        cv2.imwrite('cam.png', frame)
        
        cmd = "./darknet detector test cfg/coco.data cfg/yolo.2.0.cfg yolo.2.0.weights cam.png"# optional flag: -thresh .2"

        output = subprocess.check_output(cmd.split())

        output = output.decode("utf-8").split("\n")
        
        # Count the number of lines that contain "person"
        numPeople = len([i.split(":")[0] for i in output if i.split(":")[0] == 'person'])

        print(output[0])
        print("{} - {} people detected.".format(time.strftime("%d %b %Y %H:%M:%S", time.localtime()), numPeople))

        with open("restaurant.txt", "a") as myfile:
            myfile.write("{},{}\n".format(last, numPeople))

    # On keyboard interrupt, terminate program
    except KeyboardInterrupt:
        print("Program exiting")
        break

    # If an unknown exception occurs, print it and continue looping.
    except:
        print(sys.exc_info()[0])
        continue