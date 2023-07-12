# -*- coding: utf-8 -*-
"""
Created on Tue May 30 18:13:20 2023

@author: ifrommer
"""
import cv2
folder = r'C:\Users\ifrommer\Documents\Ian\Current Projects\CV_with_MKS\code\data'
import random
import os
#%%
def load_images_from_folder(folder):
    videos = []
    save_folder = r'C:\Users\ifrommer\Documents\Ian\Current Projects\CV_with_MKS\code\data\stills'
    for filename in os.listdir(folder):

        #vid = cv2.imread(os.path.join(folder,filename))
        vid = cv2.VideoCapture(os.path.join(folder,filename))

        if vid is not None:
            fps = vid.get(cv2.CAP_PROP_FPS)      # OpenCV v2.x used "CV_CAP_PROP_FPS"
            frame_count = int(vid.get(cv2.CAP_PROP_FRAME_COUNT))
            # duration = frame_count/fps
            # print(duration)
            rand_frame_num = random.randint(0,frame_count)
            print(rand_frame_num)
            
            vid.set(cv2.CAP_PROP_POS_FRAMES, rand_frame_num)
            ret, frame = vid.read()

            # cv2.imshow('frame', frame); cv2.waitKey(0)

            jpg_name = filename + '_' + str(rand_frame_num) + '.jpg'
            
            cv2.imwrite(os.path.join(save_folder,jpg_name), frame)

            videos.append(vid)
    return videos

videos = load_images_from_folder(folder)
#cap = cv2.VideoCapture('chaplin.mp4')

"""
	frame = get_frame(video, rand_time)
"""