#!/usr/bin/env python

import glob
import pandas as pd
from PIL import Image
import os
import sys

NEG_DIR = '/home/florian/Data/data/noaa-whales/full_data/negatives/'
POS_DIR = '/home/florian/Data/data/noaa-whales/full_data/positives/'


def gen_neg_lst():
  lst = glob.glob(NEG_DIR + '*.jpg')
  lstx = {'lst' : lst}
  lstx = pd.DataFrame(data=lstx)
  lstx.to_csv('neg.lst', header = None, index = None)
  
def gen_pos_lst():
  lst = glob.glob(POS_DIR + '*.jpg')
  with open('pos.lst', 'wb') as outfile:
    for path in lst:
      im = Image.open(path)
      w,h = im.size
      #outfile.write('%s %i %i %i %i %i\n' % (path,1,0,0,w,h))
      outfile.write('%s\t%i\t%i\t%i\t%i\t%i\n' % (path,1,0,0,w,h))
    outfile.close()

def gen_pos_vec():
  size = pd.read_csv('pos.lst', header=None).shape[0]
  command = 'opencv_createsamples -info pos.lst -num ' + str(size) + ' -w 128 -h 128 -vec pos.vec -maxxangle 360 -maxyangle 360 -maxzangle 10' 
  os.system(command)

def train_cascade():
  command = 'opencv_traincascade -data cascade -vec pos.vec -bg neg.lst -numPos 400 -numNeg 800 -numStages 3 -w 128 -h 128 -featureType HAAR -maxFalseAlarmRate 0.2'
  os.system(command)

if __name__ == '__main__':
  gen_neg_lst()
  gen_pos_lst()
  gen_pos_vec()
  train_cascade()
