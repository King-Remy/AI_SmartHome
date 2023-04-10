# Deploy tflite Object Detection model on Raspberry Pi4 and integrating Adafruit Cloud 

This is the code repository of human Detection module to perform real-time human detection using [TensorFlor Lite](https://www.tensorflow.org/lite), images streamed from a web camera and running on Edge device of Raspberry Pi to actuate a fan. It draws a bounding box around each detected object in the camera preview (when a person score is detected as 1 or above) and pushes detected people and the temperature to [Adafruit Cloud](https://www.adafruit.com/). To get started, you will have to download the example files.

First, clone this Git repo onto your Raspberry Pi like this:
```
git clone https://github.com/tensorflow/examples.git
```

## Prerequisites
* Web Camera
* Raspberry Pi
* Monitor
* Breadbroad
* Adafruit Cloud
* python 
* Opencv  
* numpy

To install the Python dependencies and EfficientDet-Lite model, run:

Create a Python virtual environment for the TFLite samples (optional but strongly recommended)
```
python3 -m venv ~/tflite
```
Run this command whenever you open a new Terminal window/tab to activate the environment.
```
source ~/tflite/bin/activate
```
Next,

```
go to examples/lite/examples/object_detection/raspberry_pi

Take the sh setup.sh and requirements.txt file and place in your working directory

# The script installs the required dependencies and download the TFLite models.
sh setup.sh
```
Next, add your Adafruit IO Key
```
Go to secret.py and paste your Adafruit username and active key for image publishing to cloud
```

Next, to run the code on Raspberry Pi, use `run.py` as follows:

```
python3 run.py 
```
## Hardware Setup

![Sensor_and_actuation_unit_bb](/Assets/Sensor_and_actuation_unit_bb.jpg)

## Result
* Human detection and fan actuation

![human_detection](/Assets/human_detection.gif)

* Adafruit Cloud dashboard of person detected
![AdafruitDashboard](/Assets/AdafruitDashboard.jpg)
![cloud1](/Assets/cloud1.png)