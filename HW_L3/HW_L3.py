#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2 as cv
import numpy as np


# In[2]:


# problem 1 


# In[ ]:


img_1 = cv.imread('pic1.jpg') 

rgb = cv.cvtColor(img_1, cv.COLOR_BGR2RGB)
cv.imshow('rgb', rgb) 

hsv = cv.cvtColor(img_1, cv.COLOR_BGR2HSV)
cv.imshow('hsv', hsv) 

lab = cv.cvtColor(img_1, cv.COLOR_BGR2LAB)
cv.imshow('lab', lab) 

gray = cv.cvtColor(img_1, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

cv.waitKey(0)


# In[ ]:


#problem 2


# In[ ]:


b, g, r = cv.split(img_1 )

blank = np.zeros(img_1.shape[:2], dtype = 'uint8')
blue = cv.merge([b, blank, blank])
green = cv.merge([blank, g, blank])
red = cv.merge([blank, blank, r])

cv.imshow('blue_grayscale', b)
cv.imshow('blue', blue)
cv.imshow('green_grayscale', g)
cv.imshow('green', green)
cv.imshow('red_grayscale', r)
cv.imshow('red', red)

cv.waitKey(0)


# In[ ]:


# problem 3


# In[ ]:


img_2 = cv.imread('pic2.jpg') 

cv.imshow('original', img_2)

average = cv.blur(img_2, (7,7))

cv.imshow('average blur', average)

bilateral1 = cv.bilateralFilter(img_2, 5, 15, 15)  

cv.imshow('bilateral_1', bilateral1)

bilateral = cv.bilateralFilter(img_2, 10, 50, 70)

cv.imshow('bilateral_2', bilateral)

cv.waitKey(0)


# In[ ]:


# problrm 4


# In[ ]:


cat = cv.imread('cat.jpg') 
blank = np.zeros(cat.shape[:2], dtype = 'uint8')

mask = cv.circle(blank, (cat.shape[1]//2, cat.shape[0]//2), 70, 255, -1)

cv.imshow('original', cat) 
cv.imshow('mask', mask) 

masked_image = cv.bitwise_and(cat, cat, mask=mask)

cv.imshow('original image', cat) 
cv.imshow('result', masked_image) 

cv.waitKey(0)


# In[ ]:


#problem 5


# In[ ]:


blank = np.zeros((400, 400, 3), dtype='uint8')

rectangle1 = cv.rectangle(blank.copy(), (30, 30), (370, 370), (130, 130, 130), -1)
rectangle2 = cv.rectangle(blank.copy(), (30, 30), (370, 370), (120, 0, 250), -1)

circle1 = cv.circle(blank.copy(), (200, 200), 200, (130, 130, 130), -1)
circle2 = cv.circle(blank.copy(), (200, 200), 200, (120, 0, 250), -1)

bitwise_xor = cv.bitwise_xor(rectangle1, circle1)
bitwise_or1 = cv.bitwise_or(rectangle1, circle1)
bitwise_xor2 = cv.bitwise_xor(rectangle2, circle2)

cv.imshow('bitwise_xor', bitwise_xor)
cv.imshow('bitwise_or1', bitwise_or1)
cv.imshow('bitwise_or2', bitwise_xor2)

cv.waitKey(0)


# In[ ]:





# In[ ]:




