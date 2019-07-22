"""
Reference: 
https://en.wikipedia.org/wiki Academic_grading_in_the_United_States
"""
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import cv2
 
img_1 = Image.open("/home/mahdi/Documents/GitHub/steganography/hossein/1.jpg") # 225.225
img_2 = Image.open("/home/mahdi/Documents/GitHub/steganography/hossein/2.jpg")
img_3 = Image.open("/home/mahdi/Documents/GitHub/steganography/hossein/3.jpg")
img_4 = Image.open("/home/mahdi/Documents/GitHub/steganography/hossein/4.jpg")

def __ghaboolMardood(grade):
		
	if grade >= 16.0:
		gradePoint = 4.0 # A
		img_4.show()
	elif grade < 16.0 and grade >=14.0:
		gradePoint = 3.0 # B
	elif grade < 14.0 and grade >=12.0:
		gradePoint = 2.0 # C
	elif grade < 12.0 and grade >=10.0:
		gradePoint = 1.0 # D
		img_1.show()
	else:
		gradePoint = 0 #F
	return gradePoint


if __name__ == "__main__":
	ramz = open("myfile.txt")
	#x = "lotfan Nomre daneshjoo ra vared konid."
	#nomreDaneshjoo = float(input(x))
	#print(__ghaboolMardood(nomreDaneshjoo))
	#print(img_1.size)
	#print(type(img_1))
	print(ramz)

	backGroundBlack = (np.zeros((255,255)))  #Meshki
	backGroundWhite = (np.ones((255,255))*255)  #Meshki

	cv2.imshow('backGround_white', backGroundWhite)
	cv2.imshow('backGround_black', backGroundBlack)
	
	cv2.waitKey()
	
	
