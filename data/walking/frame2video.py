# -*- coding: utf-8 -*-
"""
Created on Fri Apr 13 15:10:11 2018

@author: maxco
"""
import os
import cv2
cwd = os.getcwd()
filelist=[]
for file in os.listdir(cwd):
    if file.endswith(".avi"):
        filelist.append(file)

for file in filelist:        
    vidcap = cv2.VideoCapture(file)
    success,image = vidcap.read()
    count = 0
    success = True
    while success:
      success,image = vidcap.read()
      filename=str(file)+"frame"+str(count)+".jpg" 
      cv2.imwrite(filename, image)     # save frame as JPEG file
      #if cv2.waitKey(10) == 27:                     # exit if Escape is hit
       #   break
      count += 1