import cv2 as cv
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

img = cv.imread('pic1.jpg')

#1
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

gray_hist = cv.calcHist([gray], [0], None, [256], [0, 256]) 
gray_hist = [i[0] for i in gray_hist]

mpl.use('tkagg')
x = np.arange(256)
plt.plot(x, gray_hist)
plt.title('Grayscale Histogram')
plt.xlabel('Bins')
plt.ylabel('# of pixels')
plt.show()

#2
colors = ('b', 'g', 'r')

for i, col in enumerate(colors):
    hist = cv.calcHist([img], [i], None, [256], [0, 256]) 
    mpl.use('tkagg')
    x = np.arange(256)
    plt.plot(x, hist, color = col)
    plt.title('Color Histogram')
    plt.xlabel('Bins')
    plt.ylabel('# of pixels')

plt.show()


#3
cv.imshow('pic1', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

threshold, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
cv.imshow('simple threshold with thresh binary', thresh)

adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 9)
cv.imshow('adaptive threshold with mean', adaptive_thresh) 

adaptive_thresh_gaussian = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 9)
cv.imshow('adaptive threshold with gaussian', adaptive_thresh_gaussian) 

cv.waitKey(0)

#4
img = cv.imread('pic2.jpg')

cv.imshow('pic2', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

lap = cv.Laplacian(gray, cv.CV_64F)
lap = np.uint8(np.absolute(lap))

cv.imshow('laplacian', lap)

sobelx = cv.Sobel(gray, cv.CV_64F, 1, 0)
sobely = cv.Sobel(gray, cv.CV_64F, 0, 1)

cv.imshow('sobelx', sobelx)
cv.imshow('sobely', sobely)

combined_sobel = cv.bitwise_or(sobelx, sobely)

cv.imshow('combined sobel', combined_sobel) 

canny = cv.Canny(img, 125, 175)

cv.imshow('canny', canny) 

cv.waitKey(0)

