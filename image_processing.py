import cv2 as cv
import os
from shutil import copyfile
import shutil
import numpy as np

class ImageProcessor():
    current_image = ' '
    current_image_directory = ' '

    def __init__(self):
        pass

    def formatSource(self,inputString):
        index = inputString.find("file:///")
        if index != -1:
            newInputString = inputString[index + 7:]
            return newInputString.rstrip("\r\n")
        else:
            return inputString.rstrip("\r\n")

    def returnImage(self):
        return self.current_image_directory

    def setImage(self, line):
        self.current_image = line

    def setImageDirectory(self, line):
        self.current_image_directory = line

    def getImage(self, lineText):
            source = self.formatSource(lineText)
            print(source)
            destination = os.getcwd()
            head, tail = os.path.split(source)
            self.current_image = tail
            self.current_image_directory = source
            print(source)
            if(os.path.isfile(source)):
                shutil.copy(source, destination)
                self.current_image = tail
                return self.current_image
            else:
                return 'Error: file not found'


    def displayImage(self):
        if(self.isInDirectory(self.returnImage())):
            img = cv.imread(self.returnImage())
            cv.imshow('image', img)
            cv.waitKey(0)
            self.clean()
            cv.destroyAllWindows()

        else:
            return 'Error: file not found'

    def isInDirectory(self,path):

        return os.path.exists(path)

    def clean(self):
        if not self.isInDirectory(self.returnImage()):
            return 'Error: file not found'
        else:
            temp = self.returnImage()
            os.remove(self.current_image)
            return self.current_image
