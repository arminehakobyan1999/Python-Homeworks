import cv2 as cv
import numpy as np

#1
pic1 = cv.imread('pic1.jpg')
cv.imshow('Sheep', pic1)

gray = cv.cvtColor(pic1, cv.COLOR_BGR2GRAY)
cv.imshow('Black and White sheep', gray)
cv.waitKey(0)

#2
pic1 = cv.imread('pic1.jpg')
cv.imshow('Sheep', pic1)

blur_3 = cv.GaussianBlur(pic1, (3,3), cv.BORDER_DEFAULT)
cv.imshow('Blurred by 3', blur_3)

blur_11 = cv.GaussianBlur(pic1, (11, 11), cv.BORDER_DEFAULT)
cv.imshow('Blurred by 11', blur_11)

cv.waitKey(0)


#3
pic2 = cv.imread('pic2.jpg')
cv.imshow('Toucan', pic2)

canny = cv.Canny(pic2, 125, 127)
cv.imshow('Toucan_edges', canny)

blur = cv.GaussianBlur(pic2, (3,3), cv.BORDER_DEFAULT)
canny = cv.Canny(blur, 125, 127)
cv.imshow('Toucan_edges_blurred', canny)

cv.waitKey(0)


#4
pic2 = cv.imread('pic2.jpg')

pic_resize_wide = cv.resize(pic2, (pic2.shape[1] * 2, pic2.shape[0]),interpolation = cv.INTER_AREA)
cv.imshow('Toucan_wide', pic_resize_wide)

pic_resize_short = cv.resize(pic2, (pic2.shape[1], pic2.shape[0]//2),interpolation = cv.INTER_CUBIC)
cv.imshow('Toucan_short', pic_resize_short)

cv.waitKey(0)


#5
img = cv.imread('pic3.jpg') 
cv.imshow('pic3', img)

def translate(img, x, y): #image, # of pixels you want to shift in x and y axes
    
    transMat = np.float32([[1, 0, x], [0, 1, y]]) #translation matrix
    dimentions = (img.shape[1], img.shape[0]) #(width, height)
    
    return cv.warpAffine(img, transMat, dimentions)

translated = translate(img, 50, 200) 
    
cv.imshow('Translated', translated)

def rotate(img, angle, rotPoint = None):
    (height, width) = (img.shape[0], img.shape[1])
    
    if rotPoint == None:
        rotPoint = (width//2, height//2)
        
    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0) 
    dimentions = (width, height)
    
    return cv.warpAffine(img, rotMat, dimentions)

rotated = rotate(translated, 50) 
    
cv.imshow('Roteted', rotated)

flip = cv.flip(rotated, -1) 

cv.imshow('flipped', flip)


cv.waitKey(0)



#6
img = cv.imread('pic3.jpg') 

cv.imshow('pic3', img)

canny = cv.Canny(img, 125, 175)

contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)

blank = np.zeros(img.shape, dtype = 'uint8')

cv.drawContours(blank, contours, -1, (0, 0, 255), 1) 
cv.imshow('contours1', blank)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)


blur = cv.GaussianBlur(gray, (3, 3), cv.BORDER_DEFAULT)


canny = cv.Canny(blur, 125, 175)

contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)

blank = np.zeros(img.shape, dtype = 'uint8')

cv.drawContours(blank, contours, -1, (0, 0, 255), 1) 
cv.imshow('contours2', blank)

cv.waitKey(0)

