'''
from random import randint
import unicornhat as unicorn
import time
import os
import sys
import tty
import threading
import math
from pyfiglet import figlet_format
#unicorn.brightness(.5)
k=-1
unicorn.set_layout(unicorn.AUTO)
unicorn.rotation(0)
width,height=unicorn.get_shape()

obj = Line()
while True:
      old = obj.getLine()
      count=0
      for i in old:
          unicorn.set_pixel(old[count][0],old[count][1],255,0,255);
          count+=1
      unicorn.show()
      time.sleep(1)
      unicorn.clear()
      obj.rotate();
'''
from math import radians,cos,sin


'''
from Line import Line
obj = Line()
while True:
      old = obj.getLine()
      count=0
      for i in old:
          unicorn.set_pixel(old[count][0],old[count][1],255,0,255);
          count+=1
      unicorn.show()
      time.sleep(1)
      unicorn.clear()
      obj.rotate();
'''

from Line import Line
from Triangle import Triangle
print "------Original--------------------------"
obj = Line()
old = obj.getShape();
print old
print "------Rotated---------------------------"
xy = obj.rotate()
print xy
'''
print "------Original Now Rotated--------------"
old = obj.getLine();
print old

print "------Original Now Rotated Again--------"
xy = obj.rotate()
print xy
count = 0
for j in xy:
    print str(int(xy[count][0])) +" "+ str(int(xy[count][1]))
    count+=1'''
