# problem 1


import cv2 as cv


img1 = cv.imread('pic1.jpg')
img2 = cv.imread('pic2.jpg')
img3 = cv.imread('pic3.jpg')



cv.imshow('pic1', img1)
cv.imshow('pic2', img2)
cv.imshow('pic3', img3)
cv.waitKey(0)


# problem 2



cap = cv.VideoCapture('vid1.mp4')

if (cap.isOpened()== False): 
    print("Error opening video stream or file")

while(cap.isOpened()):
    ret, vid = cap.read()
    if ret == True:
        cv.imshow('vid1',vid)

        if cv.waitKey(25) & 0xFF == ord('q'):
            break
    else: 
        break

cap.release()
cv.destroyAllWindows()
cv.waitKey(0)


# problem 3



scale_percent = 0.5

width = int(img1.shape[1] * scale_percent)
height = int(img1.shape[0] * scale_percent)

dsize = (width, height)
output = cv.resize(img1, dsize, interpolation=cv.INTER_AREA)
cv.imshow('pic', img1)
cv.imshow('pic_rescale', output)


cv.waitKey(0)


# problem 4



cap = cv.VideoCapture('vid1.mp4')

scale_percent = 0.5


if (cap.isOpened()== False): 
    print("Error opening video stream or file")

while (cap.isOpened()):
    ret, vid = cap.read()
    if ret == True:
        width = int(vid.shape[1] * scale_percent)
        height = int(vid.shape[0] * scale_percent)
        dsize = (width, height)
        cv.imshow('vid1',vid)
        output = cv.resize(vid, dsize, interpolation=cv.INTER_AREA)
        cv.imshow('Video_rescaled', output)
        
        if cv.waitKey(25) & 0xFF == ord('q'):
            break
    else: 
        break

cap.release()
cv.destroyAllWindows()
cv.waitKey(0)


# problem 5



img_circle = cv.imread('pic2.jpg')
cv.circle(img_circle,(img_circle.shape[1]//2, img_circle.shape[0]//2), img_circle.shape[0]//3, (0, 0, 255), thickness = -1)

cv.imshow('With_Circle', img_circle)
cv.imshow('Original', img2)
cv.waitKey(0)


# problem 6


img_rectangle = cv.imread('pic2.jpg')

cv.rectangle(img_rectangle, (img_rectangle.shape[1]//4, img_rectangle.shape[0]//4), 
             (img_rectangle.shape[0] - img_rectangle.shape[0]//4,img_rectangle.shape[1] - img_rectangle.shape[1]//4),
             (0, 165, 255), thickness = 2)

cv.imshow('With_Rectangle', img_rectangle)
cv.imshow('Original', img2)
cv.waitKey(0)


# problem 7


img_line = cv.imread('pic1.jpg')

cv.line(img_line, (0,img_line.shape[0]), (img_line.shape[1], 0),(0, 255, 0), thickness = 3)

cv.imshow('With_Line', img_line)
cv.imshow('Original', img1)
cv.waitKey(0)

