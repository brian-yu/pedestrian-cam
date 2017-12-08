# Pedestrian Cam
## 	Counting Foot Traffic Over IP Webcams with Machine Learning

This is the repository for the project talked about in this [blog post](https://www.byu.io/2017/12/07/counting-people-with-ml). 

## How to get up and running:
1. Clone YOLO & Darknet
	```bash
	git clone https://github.com/pjreddie/darknet
	```

2. Clone this repository into the same directory
	```bash
	git clone https://github.com/brian-yu/pedestrian-cam.git
	mv pedestrian-cam/* .
	rm -r pedestrian-cam
	```

3. Run the files
	For the webserver, run `server.py` and `prediction.py`
	Otherwise, you can explore the Jupyter notebooks.