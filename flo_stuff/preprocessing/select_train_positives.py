#!/usr/bin/env python

import pandas as pd
import os
import glob
from PIL import Image

all_pos_dir = '../positive_imgs/'	# Directory with all positive samples
train_lst = 'train.csv'			# train.csv File from Kaggle download

train_pos_dir = '/home/florian/Data/data/noaa-whales/full_data/positives/'	# Output Directory for train-positive samples

def select_train_positives():
  train_lst = pd.read_csv(train_lst, delimiter=',')
  pos = glob.glob(all_pos_dir + '*.jpg')
  pos = [i.split('/')[-1] for i in pos]
  
  with open('positives.csv', 'wb') as outfile:
    for i, line in enumerate(train_lst.iterrows()):
      line = line[1]['Image']
      #command = "cp ../positive_imgs/" + line + " positives"
      if line in pos:
	im = Image.open(all_pos_dir + line)
	im = im.resize((128, 128), Image.ANTIALIAS)
	im.save('positives/'+line)
	path = train_pos_dir + line
	posi = '[' + str(0) + ',' + str(0) + ',' + str(128) + ',' + str(128) + ']'
	outfile.write('%s\t%s\n' % (path,posi) )
    outfile.close()

if __name__ == '__main__':
  
  select_train_positives()
