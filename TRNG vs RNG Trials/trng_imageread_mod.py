# This template is to read true random numbers from processed image, it will return a 6 digit number from 0 to 1. 
# This template reads numbers by order of pixels, you can easily randomly read them with other functions random.random()

import cv2
import numpy
import math
import random

def trRead(i):    #read image number i
    
    pic_path = "C:\\Users\\Jorge\\OneDrive - Worcester Polytechnic Institute (wpi.edu)\\Fall 2020\\CS534 - AI\\CS534 - Project\\Random tank\\True random jpg tank\\TRN%d.jpg" %i 
    image = cv2.imread(pic_path)
    return image

def trNum(image,i,j):     #generate a 6 digit true random number from 0 to 1

    a = image[i,j]
    #print (a)
    b = (a[0]%100)*10**(-2)+(a[1]%100)*10**(-4)+(a[2]%100)*10**(-6)
    return b

def count():   #must count the use of pics
    pc = 99     #the current image number value between 1 to 100 (or higher)
    ptw = 0     #current position of reading number
    pth = 0
    img = trRead(pc)
    i = 0
    datalist = []
    while i <= 5999999/1.01:   # depens on how many numbers needed, use this as template to write other functions, this is a test print
        c = trNum(img, int(ptw), int(pth))  #get a true random number from current image
        datalist.append (c)
        #print ('%.6f' %c)
        #print (ptw)
        i = i + 1
        if pth >= 2999:
            pc = pc + 1
            img = trRead(pc)
            pth = 0
            ptw = 0
        elif ptw >= 1999:
            ptw = 0
            pth += 1
        else:
            ptw += 1
    print ('Done')
    return datalist

data = count()

dataFile = open('TRNG txt data.txt', 'w')
for eachitem in data:
    dataFile.write(str(eachitem)+'\n')
dataFile.close()

'''

def generatetxt():
    pc = 1     
    pt = 0     
    img = trRead(pc)
    i = 0
    while i <= 500:   # depens on how many numbers needed, use this as template to write other functions, this is a test print
        c = trNum(img, int(pt%3000), int(pt%2000))  #get a true random number from current image
        print ('%.6f' %c)
        i = i + 1
        if pt >= 5999999:
            pc = pc + 1
            img = trRead(pc)
            pt = 0
        else:
            pt = pt + 1

count()
    
'''
