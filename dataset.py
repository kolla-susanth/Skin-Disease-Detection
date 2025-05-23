from roboflow import Roboflow
rf = Roboflow(api_key="")  # add api that is used in roboflow for data anotation 
project = rf.workspace("skin-diseases-jzde4").project("skin-diseases-i30ay")
version = project.version(1)
dataset = version.download("yolov8")
