import math
import cv2
import csv
import os

def read_bmp(image_name):
	return cv2.imread(image_name+'.bmp')

def calculate_psnr(n):
	s = read_bmp('source/s'+n)
	r = read_bmp('recovery/rs'+n)

	height, width, channel = s.shape
	size = height*width

	sb,sg,sr = cv2.split(s)
	rb,rg,rr = cv2.split(r)

	mseb = ((sb-rb)**2).sum()
	mseg = ((sg-rg)**2).sum()
	mser = ((sr-rr)**2).sum()

	MSE = (mseb+mseg+mser)/(3*size)
	psnr = 10*math.log10(255**2/MSE)
	return round(psnr,2)

def write_csv(n,data):
	with open('PSNR-result/'+n+'.csv', 'w', newline='') as myfile:
		wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
		wr.writerow(data)

for i in range(6):
	print("Creating CSV of PSNR-result",i+1,"...",sep="")
	write_csv(str(i+1),[calculate_psnr(str(i+1))])

os.system("pause")