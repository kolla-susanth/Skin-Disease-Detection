from roboflow import Roboflow
rf = Roboflow(api_key="qDw7LTKhpnlGOw81ntqH")
project = rf.workspace("skin-diseases-jzde4").project("skin-diseases-i30ay")
version = project.version(1)
dataset = version.download("yolov8")
