#!/usr/bin/env python

'''
Create sample data for cascade classifier
- positive samples read from POS_DIR
- negative samples read from NEG_DIR
- writes jpg's to OUT_DIR

'''

from PIL import Image
import numpy as np
import os

angles = [0, 90, 180, 270]

def create_samples(pos_dir, neg_dir, out_dir):

	positive_lst = os.listdir(pos_dir)
	negative_lst = os.listdir(neg_dir)

	with open(out_dir + 'info.lst', 'wb') as infoFile:
		for p, path in enumerate(positive_lst):
			print('Processing Image: %s, num: %i/%i' % (path, p, len(positive_lst)))

			negatives = np.random.choice(negative_lst, 4)
			#print negatives

			for n, neg_path in enumerate(negatives):
				for a, ang in enumerate(angles):
				
					#print neg_path, n
					#print path
					#print a, ang

					positive = Image.open(pos_dir + path)
					negative = Image.open(neg_dir + neg_path)

					negative_size = negative.size

					rand_size = np.random.randint(200, 500)
					rand_pos1 = np.random.randint(0, (negative_size[0] - rand_size))
					rand_pos2 = np.random.randint(0, (negative_size[1] - rand_size))


					positive = positive.rotate(ang, resample=Image.BICUBIC, expand = True)
					positive = positive.resize((rand_size, rand_size), Image.ANTIALIAS)


					negative.paste(positive, (rand_pos1,rand_pos2))
					negative.save(out_dir + str(ang) + '_' + str(n) + path)

					#0001_0385_0089_0243_0243.jpg 1 385 89 243 243
					info_entry = str(ang) + '_' + str(n) + path
					infoFile.write('%s %s %s %s %s %s\n' % (info_entry, '1', str(rand_pos1), str(rand_pos2), str(positive.size[0]), str(positive.size[1])))




if __name__ == '__main__':

	POS_IN_DIR = '/home/jean/Kaggle/Wale/Nick/data/train_pos/'
	NEG_IN_DIR = '/home/jean/Kaggle/Wale/Nick/data/train_neg/'
	OUT_DIR = '/home/jean/Kaggle/Wale/Nick/data/samples/'

	create_samples(POS_IN_DIR,NEG_IN_DIR,OUT_DIR)
