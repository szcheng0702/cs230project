# -*- coding: utf-8 -*-
"""
Created on Sat Apr 21 14:39:53 2018

@author: maxco
"""

import os
import cv2
import numpy as np
import tensorflow as tf
import natsort   
import matplotlib.pyplot as plt    


def sample(collection,index=0,gap=1):
    before=collection[index]
    after=collection[index+2*gap]
    mid=collection[index+gap]
    return before, after, mid
    
def show_sample_train(collection,batch_size, gap):
    before, after, mid = sample(collection,index=20,gap=gap)
    print("Range of Image Piece Value: [{}, {}]".format(np.min(mid), np.max(mid)))
    #print("Before: {}".format(before.shape))
    #print("After:  {}".format(after.shape))
    #print("Mid:    {}".format(mid.shape))
    size = (20, 2)
    plot_images(before, size, "Before")
    plot_images(mid, size, "Mid")
    plot_images(after, size, "After")
    return 0

def read_data(subfile="\jpg\\"):
    cwd = os.getcwd()
    filelist=[]
    for file in os.listdir(cwd+subfile):
        if file.endswith(".jpg"):
            filelist.append(file)
    filelist = natsort.natsorted(filelist)        
    training_data = []
    IMG_SIZE=32
    
    for path in filelist[:100]:
        img_data = cv2.imread(cwd+subfile+path, cv2.IMREAD_GRAYSCALE)
        img_data = cv2.resize(img_data, (IMG_SIZE, IMG_SIZE))
        training_data.append([np.array(img_data)])
    return training_data

def plot_img(img, size = None, ax=None):
    max_val = np.max(img)
    if size: plt.figure(figsize=size)
    if 'float' in str(img.dtype) and max_val < 10:
        plt.imshow(convert_for_display(img))
    else:
        plt.imshow(img,cmap='gray')
    return

def plot_images(imgs, size = (12, 6), title=None, sub_titles=[]):
    """
    Input: 
        imgs: [image]
    """
    fig = plt.figure(figsize=size)
    for i, img in enumerate(imgs):
        ax = fig.add_subplot(1, len(imgs), i+1)
        if img.shape[-1] == 1: img = img.reshape(img.shape[:-1]) # in case of one channel
        if sub_titles: plt.title(sub_titles[i])
        plot_img(img)
        ax.set_xticklabels([])
        ax.set_yticklabels([])
    if title: plt.suptitle(title)
    plt.show()
    return

def main():
    all_data=read_data()
    show_sample_train(all_data,batch_size = 8, gap = 2)
    plt.show()
    return 0