# -*- coding: utf-8 -*-
"""
Created on Mon May 14 18:02:18 2018

@author: maxco
"""

import cv2
import numpy as np
import os
cwd = os.getcwd()
files=os.listdir(cwd)[:-1]

for file in files:
    cap = cv2.VideoCapture(file)
    frameCount = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    frameWidth = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frameHeight = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    
    buf = np.empty((frameCount, frameHeight, frameWidth, 3), np.dtype('uint8'))
    
    fc = 0
    ret = True
    
    while (fc < frameCount  and ret):
        ret, buf[fc] = cap.read()
        fc += 1
    
    cap.release()
    
    grsc = np.empty((frameCount,32, 32), np.dtype('uint8'))
    
    for i,elem in enumerate(buf):
        grsc[i] = cv2.normalize(cv2.resize( cv2.cvtColor(elem, cv2.COLOR_BGR2GRAY), (32, 32)).astype(np.float64), None, 0.0, 1.0, cv2.NORM_MINMAX)
        #d1={, 'info':file[:-4]}
    np.savez(file[:-4],imgs=grsc,info=file[:-4])


