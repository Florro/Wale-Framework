#!/usr/env/bin python

'''
Create Positive samples images from jeans list
- read data from 'IN_DIR'
- write positives to 'OUT_DIR'

'''

IN_DIR = './imgs_subset/'
OUT_DIR = './jeanheads/'


import pandas as pd
import os
from PIL import Image




def create_positives():
        if not os.path.exists(OUT_DIR):
            os.makedirs(OUT_DIR)

	tmp = pd.read_csv('./positive_positions.csv', delimiter='\t', header=None)

	d = { 'pos' : tmp[1], 'path' : tmp[0] }
	position_lst = pd.DataFrame(data=d)

	position_lst['pos'] = position_lst['pos'].apply(lambda s:s.replace('[', ''))
	position_lst['pos'] = position_lst['pos'].apply(lambda s:s.replace(']', ''))


	position_lst['path'] = position_lst['path'].apply(lambda s:s.replace("'", ''))
	position_lst['path'] = position_lst['path'].apply(lambda s:s.replace("/home/jean/Kaggle/Wale/imgs_subset/", ''))

	print position_lst['pos']
	print position_lst['path']

	for line in position_lst.iterrows():
		pos = line[1]['pos']
		pos = pos.strip().split(' ')
		pos = [int(i) for i in pos]
		inpath = IN_DIR + line[1]['path']
		outpath = OUT_DIR + line[1]['path']
		#print pos, outpath

		im = Image.open(inpath)

		# only take squares
		width = max(pos[2], pos[3])	

		im.crop((pos[0], pos[1], pos[0] + width, pos[1] + width)).save(outpath)
		#im.crop((0, 0, 1000, 1000)).save('test.jpg')

		


if __name__ == '__main__':
	create_positives()
