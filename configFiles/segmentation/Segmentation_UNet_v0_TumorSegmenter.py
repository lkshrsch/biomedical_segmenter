#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 10 10:34:06 2018

@author: lukas
"""

import os
wd = os.getcwd()

import tensorflow as tf
config = tf.ConfigProto()
config.gpu_options.allow_growth = True
config.gpu_options.visible_device_list="1"
tf.keras.backend.set_session(tf.Session(config=config))

###################   parameters // replace with config files ########################

dataset = 'MSKCC'

############################## Load dataset #############################
 
TPM_channel = ''

segmentChannels = ['/CV_folds/CV_Replicate_Aug2019/test_t1post.txt',
		 '/CV_folds/CV_Replicate_Aug2019/test_sub1.txt',
		 '/CV_folds/CV_Replicate_Aug2019/test_sub2.txt',
		 '/CV_folds/CV_Replicate_Aug2019/test_TPM.txt']
segmentLabels = ''

output_classes = 2
    
#-------------------------------------------------------------------------------------------------------------

# Parameters 

######################################### MODEL PARAMETERS

model = 'UNet_v0_TumorSegmenter' 
dpatch= [3,512,512]
segmentation_dpatch = [3,512,512]
model_patch_reduction = [2,0,0]
model_crop = 0 # 40 for normal model.

using_unet_breastMask = False
resolution = 'high'

path_to_model = '/home/deeperthought/Projects/MultiPriors_MSKCC/training_sessions/UNet_v0_TumorSegmenter_breastMask_UNet_v0_TumorSegmenter_2019-12-27_1850/models/rSegmenter_breastMask_UNet_v0_TumorSegmenter_2019-12-27_1850.log_epoch23.h5'
session =  path_to_model.split('/')[-3]

########################################### TEST PARAMETERS
use_coordinates = True
quick_segmentation = True
output_probability = True 
dice_compare = False
save_as_nifti = True  
OUTPUT_PATH = '/home/deeperthought/Projects/MultiPriors_MSKCC/training_sessions/UNet_v0_TumorSegmenter_breastMask_UNet_v0_TumorSegmenter_2019-12-27_1850/predictions/epoch23/'
percentile_normalization = True
full_segmentation_patches = True
test_subjects = 278
n_full_segmentations = 278
list_subjects_fullSegmentation = range(278)
size_test_minibatches = 32
saveSegmentation = True

import numpy as np
penalty_MATRIX = np.array([[ 1,  0],
			   [ 0,  1]], dtype='float32')

comments = ''

