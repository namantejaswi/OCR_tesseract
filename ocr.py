import numpy
import cv2 as cv
import pytesseract as pyt   
from pytesseract import Output


image=cv.imread('sbi_f.jpg')


# grey scaling the image 

grey_image= cv.cvtColor(image,cv.COLOR_BGR2GRAY)

cv.imshow('orignal',image)
cv.imshow('Greyscaled Image',grey_image)
cv.waitKey(10000)   #wait for 1o seconds

# upscaling the image to read smaller charecters

up_img = cv.resize(grey_image, None, fx=1.5, fy=1.5, interpolation=cv.INTER_AREA)
cv.imshow('upscaled',up_img)
cv.waitKey(10000)

text=pyt.image_to_string(up_img)
print(text)

fileobj=open('result.txt','a')
fileobj.write(text)


cv.destroyAllWindows
