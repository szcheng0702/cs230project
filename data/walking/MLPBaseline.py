# -*- coding: utf-8 -*-
"""
Created on Sat Apr 21 14:39:53 2018

@author: maxco
"""

import os
import cv2
import numpy as np

cwd = os.getcwd()
filelist=[]
for file in os.listdir(cwd+"\jpg"):
    if file.endswith(".jpg"):
        filelist.append(file)
        
training_data = []
IMG_SIZE=32

for path in filelist[:100]:
    img_data = cv2.imread(cwd+"\jpg\\"+path, cv2.IMREAD_GRAYSCALE)
    img_data = cv2.resize(img_data, (IMG_SIZE, IMG_SIZE))
    training_data.append([np.array(img_data)])

def sample(collection,index=0,gap=1):
    before=collection[0]
    after=collection[2]
    mid=collection[1]
    return before, after, mid
    
def show_sample_train(collection,batch_size, gap):
    before, after, mid = sample(collection,index=0,gap=1)
    print("Range of Image Piece Value: [{}, {}]".format(np.min(mid), np.max(mid)))
    print("Before: {}".format(before.shape))
    print("After:  {}".format(after.shape))
    print("Mid:    {}".format(mid.shape))
    size = (20, 2)
    plot_images(before, size, "Before")
    plot_images(mid, size, "Mid")
    plot_images(after, size, "After")
    
show_sample_train(batch_size = 8, gap = 9)