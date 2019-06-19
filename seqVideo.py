## -*- coding: utf-8 -*-
#"""
#Created on Thu Jun  6 12:32:01 2019
#
#@author: VS

#this code creates a video from a list of jpg files stored in a folder
# it uses the libray openCV 

import os
import cv2

def main():
    """
    Thi is the main program
    """
    location = os.getcwd()
    images = []
    fps = 10
    try:
        filenames = sorted((fn for fn in os.listdir(location) if fn.endswith('.jpg'))) # this iteration technique has no built in order, so sort the frames
        for filename in filenames:
            fm = cv2.imread(filename)
            images.append(fm)
        height, width, layers = fm.shape
        size = (width,height) 
        outFile = cv2.VideoWriter('seq.avi',cv2.VideoWriter_fourcc(*'DIVX'), fps, size)
        for i in range(len(images)):
            outFile.write(images[i])
        outFile.release()    
            
            
    except Exception as e:
        raise e
        print("No image files in here!")

if __name__ == "__main__":
    main()

