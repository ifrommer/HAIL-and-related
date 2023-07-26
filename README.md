# HAIL-and-related

### some progress
- burned Ring videos downloaded to **Son. machine** and copied these to **Lambda**
- ran yolo on one ring video on the **Lambda** - took 6s, did a decent job   [7/6/23 ]
- ran yolo on a ring video on the **nano**
- did some stuff before
  - **python** to batch download ring on **Son. machine**

### in progress
- identifying who is in which video manually, see *ring_files_info.csv* in some dir on machines as the videos (will upload a copy here)

### next up 
- run  Yolo on the videos on the lambda to get a rough cut of the boxes and labels
- Move Ring videos (prob from Son. laptop) to roboflow for labelling or refine lambda yolo results (see above) but on Roboflow
  -   find ones that have a variety of people and cars
- label some ring videos with people and car names - try running Yolo on the first to see if it can do the labeling for you
- retrain 
- test
