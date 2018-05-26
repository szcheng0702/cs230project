# -*- coding: utf-8 -*-
"""
Created on Mon May 14 15:54:45 2018

@author: maxco
"""

import sys
sys.path.append('..')
from util import *
from util.parser import *
from util.img_kit import *
from util.notebook_display import *
from util.numeric_ops import *
from util.tf_ops import *
from time import time

from IPython import display
import numpy as np
from scipy import ndimage
from scipy import misc
from os import walk
import os
import tensorflow as tf
from PIL import Image

import matplotlib.pyplot as plt
#%matplotlib inline
plt.rcParams['image.interpolation'] = 'nearest'
plt.rcParams['figure.figsize'] = (5.0, 5.0) # set default size of plots
plt.rcParams['image.cmap'] = 'gray'

#%load_ext autoreload
#%autoreload 2

path="../data/data/walking/32x32/train/person01_walking_d1_uncomp.npy"

sample=np.load(path)
print(sample.files)
img=sample['imgs']