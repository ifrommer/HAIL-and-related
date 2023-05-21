Do this:

workon yolov7

cd yolo/yolov7

cfg            hubconf.py        scripts
data           inference         test.py
deploy         LICENSE.md        tools
detect_idf.py  models            torch-1.8.0-cp36-cp36m-linux_aarch64.whl
detect.py      paper             traced_model.pt
export.py      README.md         train_aux.py
figure         requirements.txt  train.py
.git           runs              utils
.gitignore     run.txt           yolov7-tiny.pt

infererence/images/horses.jpg, ...

runs stored in runs/detect/exp#:
orda@ubuntu:~/yolo/yolov7/runs/detect$ ls
exp  exp2  exp3  exp4  exp5  exp6  exp7

running it on the kids_running.mp4 file

medium article:
YOLOv7 Training on Custom Data?
https://tinyurl.com/bdze4eyr

python detect.py --weights yolov7-tiny.pt --source inference/images/horses.jpg --img 640

Explanation:
--weights yolov7-tiny.pt - tells yolo which weights file to use; originally this said yolov7.pt, but that 
is not in the folder as is, and since I did see the -tiny.py one, I changed it to that, which seems to be working.
