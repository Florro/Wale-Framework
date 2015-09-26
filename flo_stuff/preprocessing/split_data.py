#!/usr/bin/env python

import pandas as pd
import os

def split_data():
  
  train_lst = pd.read_csv('train.csv', delimiter=',')
  for line in train_lst.iterrows():
    line = line[1]['Image']
    command = "mv test/" + line + " train"
    os.system(command)
  

if __name__ == '__main__':
  split_data()
  
  