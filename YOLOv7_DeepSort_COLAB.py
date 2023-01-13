# -*- coding: utf-8 -*-

# Commented out IPython magic to ensure Python compatibility.
!git clone https://github.com/Azfe38/YOLOv7_DeepSort_COLAB
# %cd YOLOv7_DeepSort_COLAB

!wget https://github.com/WongKinYiu/yolov7/releases/download/v0.1/yolov7x.pt

from detection_helpers import *
from tracking_helpers import *
from  bridge_wrapper import *
from PIL import Image

detector = Detector(classes = None) # [person,horses,sports ball] olarak özelleştirilebilir. class = None sınıf ayırt etmez. Tüm sınıflar için : "data/coco.yaml"
detector.load_model('./yolov7x.pt',) # pass the path to the trained weight file

# Pass in any image path or Numpy Image using 'BGR' format
result = detector.detect('./IO_data/input/images/horses.jpg', plot_bb = True) # plot_bb = False output the predictions as [x,y,w,h, confidence, class]


if len(result.shape) == 3:# If it is image, convert it to proper image. detector will give "BGR" image
    result = Image.fromarray(cv2.cvtColor(result,cv2.COLOR_BGR2RGB)) 
    
result

# Initialise  class that binds detector and tracker in one class
tracker = YOLOv7_DeepSORT(reID_model_path="./deep_sort/model_weights/mars-small128.pb", detector=detector)

# output = None will not save the output video
tracker.track_video("./IO_data/input/video/street.mp4", output="./IO_data/output/street.avi", show_live = False, skip_frames = 0, count_objects = True, verbose=1)

!pip install ffmpeg-python

cd content

ls

cd yolov7-deepsort-tracking/

ls

cd IO_data/

# Commented out IPython magic to ensure Python compatibility.
# convert resulting video from avi to mp4 file format
import os
path_video = os.path.join("output","street.avi")
# %cd IO_data/output
!ffmpeg -y -loglevel panic -i street.avi new_street.mp4
# %cd ..

# output object tracking video
path_output = os.path.join("output","new_street.mp4")

from IPython.display import HTML
from base64 import b64encode

ls

cd output/

mp4 = open('new_street.mp4','rb').read()
data_url = "data:video/mp4;base64," + b64encode(mp4).decode()
HTML("""<video width=900 controls><source src="%s" type="video/mp4"></video>""" % data_url)

from google.colab import drive
drive.mount('/content/drive')

from google.colab import files
!zip -r /content/yolov7-deepsort-tracking.zip /content/yolov7-deepsort-tracking

import shutil
colab_link = "/content/yolov7-deepsort-tracking.zip"
gdrive_link = "/content/drive/MyDrive"
shutil.copy(colab_link, gdrive_link)

"""Yeni videolar"""

ls

cd ..

cd ..

# Initialise  class that binds detector and tracker in one class
tracker = YOLOv7_DeepSORT(reID_model_path="./deep_sort/model_weights/mars-small128.pb", detector=detector)

# output = None will not save the output video
tracker.track_video("./IO_data/input/video/cars.mp4", output="./IO_data/output/cars.avi", show_live = False, skip_frames = 0, count_objects = True, verbose=1)

# Initialise  class that binds detector and tracker in one class
tracker = YOLOv7_DeepSORT(reID_model_path="./deep_sort/model_weights/mars-small128.pb", detector=detector)

# output = None will not save the output video
tracker.track_video("./IO_data/input/video/highway.mp4", output="./IO_data/output/highway.avi", show_live = False, skip_frames = 0, count_objects = True, verbose=1)

# Initialise  class that binds detector and tracker in one class
tracker = YOLOv7_DeepSORT(reID_model_path="./deep_sort/model_weights/mars-small128.pb", detector=detector)

# output = None will not save the output video
tracker.track_video("./IO_data/input/video/intersection.mp4", output="./IO_data/output/intersection.avi", show_live = False, skip_frames = 0, count_objects = True, verbose=1)

# Initialise  class that binds detector and tracker in one class
tracker = YOLOv7_DeepSORT(reID_model_path="./deep_sort/model_weights/mars-small128.pb", detector=detector)

# output = None will not save the output video
tracker.track_video("./IO_data/input/video/road.mp4", output="./IO_data/output/road.avi", show_live = False, skip_frames = 0, count_objects = True, verbose=1)

ls

cd  IO_data/

ls

cd output/

# Commented out IPython magic to ensure Python compatibility.
# convert resulting video from avi to mp4 file format
import os
path_video = os.path.join("output","cars.avi")
# %cd IO_data/output
!ffmpeg -y -loglevel panic -i cars.avi cars.mp4
# %cd ..

# output object tracking video
path_output = os.path.join("output","cars.mp4")

ls

cd IO_data/

cd output/

# Commented out IPython magic to ensure Python compatibility.
# convert resulting video from avi to mp4 file format
import os
path_video = os.path.join("output","highway.avi")
# %cd IO_data/output
!ffmpeg -y -loglevel panic -i highway.avi highway.mp4
# %cd ..

# output object tracking video
path_output = os.path.join("output","highway.mp4")

ls

cd output/

# Commented out IPython magic to ensure Python compatibility.
# convert resulting video from avi to mp4 file format
import os
path_video = os.path.join("output","intersection.avi")
# %cd IO_data/output
!ffmpeg -y -loglevel panic -i intersection.avi intersection.mp4
# %cd ..

# output object tracking video
path_output = os.path.join("output","intersection.mp4")

ls

cd output/

# Commented out IPython magic to ensure Python compatibility.
# convert resulting video from avi to mp4 file format
import os
path_video = os.path.join("output","road.avi")
# %cd IO_data/output
!ffmpeg -y -loglevel panic -i road.avi road.mp4
# %cd ..

# output object tracking video
path_output = os.path.join("output","road.mp4")

ls

cd output/

mp4 = open('cars.mp4','rb').read()
data_url = "data:video/mp4;base64," + b64encode(mp4).decode()
HTML("""<video width=1024 controls><source src="%s" type="video/mp4"></video>""" % data_url)

ls

mp4 = open('highway.mp4','rb').read()
data_url = "data:video/mp4;base64," + b64encode(mp4).decode()
HTML("""<video width=1024 controls><source src="%s" type="video/mp4"></video>""" % data_url)

mp4 = open('intersection.mp4','rb').read()
data_url = "data:video/mp4;base64," + b64encode(mp4).decode()
HTML("""<video width=1024 controls><source src="%s" type="video/mp4"></video>""" % data_url)

mp4 = open('road.mp4','rb').read()
data_url = "data:video/mp4;base64," + b64encode(mp4).decode()
HTML("""<video width=1024 controls><source src="%s" type="video/mp4"></video>""" % data_url)

from google.colab import files
!zip -r /content/yolov7-deepsort-tracking_2.zip /content/yolov7-deepsort-tracking

import shutil
colab_link = "/content/yolov7-deepsort-tracking_2.zip"
gdrive_link = "/content/drive/MyDrive"
shutil.copy(colab_link, gdrive_link)