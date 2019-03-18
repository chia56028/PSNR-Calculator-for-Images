import numpy as np
import cv2
import os

def read_bmp(image_name):
	return cv2.imread(image_name+'.bmp')

def read_and_convert_image_to_LAB(image_name):
	x = cv2.imread(image_name+'.bmp')
	return cv2.cvtColor(x,cv2.COLOR_BGR2LAB)

def get_mean_and_std(x):
	x_mean, x_std = cv2.meanStdDev(x)
	x_mean = np.hstack(np.around(x_mean,2))
	x_std = np.hstack(np.around(x_std,2))
	return x_mean, x_std

def color_transfer(n):
	print("Converting picture"+n+"...")

	s = read_and_convert_image_to_LAB('source/s'+n)
	t = read_and_convert_image_to_LAB('target/t'+n)

	s_mean, s_std = get_mean_and_std(s)
	t_mean, t_std = get_mean_and_std(t)

	height, width, channel = s.shape
	for i in range(0,height):
		for j in range(0,width):
			for k in range(0,channel):
				x = s[i,j,k]
				x = ((x-s_mean[k])*(t_std[k]/s_std[k]))+t_mean[k]
				# round or +0.5
				x = round(x)
				# boundary check
				x = 0 if x<0 else x
				x = 255 if x>255 else x
				s[i,j,k] = x

	s = cv2.cvtColor(s,cv2.COLOR_LAB2BGR)
	cv2.imwrite('result/tr'+n+'.bmp',s)

def reverse_of_color_transfer(n):
	print("Recovering picture"+n+"...")

	s = read_and_convert_image_to_LAB('source/s'+n)
	t = read_and_convert_image_to_LAB('target/t'+n)
	s_mean, s_std = get_mean_and_std(s)
	t_mean, t_std = get_mean_and_std(t)

	r = read_and_convert_image_to_LAB('result/tr'+n)

	height, width, channel = r.shape
	for i in range(0,height):
		for j in range(0,width):
			for k in range(0,channel):
				x = r[i,j,k]
				x = ((x-t_mean[k])*(s_std[k]/t_std[k]))+s_mean[k]
				# round or +0.5
				x = round(x)
				# boundary check
				x = 0 if x<0 else x
				x = 255 if x>255 else x
				r[i,j,k] = x

	r = cv2.cvtColor(r,cv2.COLOR_LAB2BGR)
	cv2.imwrite('recovery/rs'+n+'.bmp',r)


for i in range(6):
	color_transfer(str(i+1))
	# reverse
	reverse_of_color_transfer(str(i+1))

os.system("pause")