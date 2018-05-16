# -*- coding: utf-8 -*-
"""
Created on Sun Apr 29 20:08:40 2018

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