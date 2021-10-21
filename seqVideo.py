## -*- coding: utf-8 -*-
#"""
#Created on Thu Jun  6 12:32:01 2019
#
#@author: VS

import os
import cv2

def main():

    """
    Thi is the main program
    """
    location = os.getcwd()
    images = []
    fps = 25
    outFile = ""
    font                   = cv2.FONT_HERSHEY_SIMPLEX
    fontScale              = 0.5
    fontColor              = (0,0,0)
    lineType               = 1
    
    try:
        filenames = sorted((fn for fn in os.listdir(location) if (fn.endswith('.jpeg') or fn.endswith('.jpg') or fn.endswith('.png')))) # this iteration technique has no built in order, so sort the frames
        for filename in filenames:
            fm = cv2.imread(filename)
            height, width, layers = fm.shape
            time_text = "Flow time = "
            if filename.endswith(".jpg"):
                time_text_fig =  time_text + filename[-14:-5] + " sec"
            elif filename.endswith(".jpeg"):
                time_text_fig =  time_text + filename[-15:-6] + " sec"
            elif filename.endswith(".png"):
                time_text_fig =  time_text + filename[-14:-5] + " sec"
            
            cv2.putText(fm, time_text_fig,
                        (5,height-10),
                        font,
                        fontScale,
                        fontColor,
                        lineType)
            images.append(fm)
        height, width, layers = fm.shape
        size = (width, height) 
        outFile = cv2.VideoWriter('seq.avi',cv2.VideoWriter_fourcc(*'DIVX'), fps, size)
        for i,im in enumerate(images):
            outFile.write(im)
        print("Number of processed images = ", i)
        cv2.destroyAllWindows()
        outFile.release()    
            
            
    except Exception as e:
        raise e
        print("No image files in here!")
    return filenames

if __name__ == "__main__":
    F = main()
    #print(F)
    #out = input("Tap a button to close ....\n ")
