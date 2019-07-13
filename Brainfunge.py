import fileinput
import sys

#ALL Setup

#Input and Memory
sourceInput = []
tape = [0] * (sys.maxsize / 2)
#Constant Directions
RIGHT = (0, 1)
LEFT = (0, -1)
UP = (-1, 0)
DOWN = (1, 0)
MAXINT = sys.maxsize

direction = RIGHT
pos = (0, 0)

for line in fileinput.input():
    sourceInput.append(line.rstrip("\r\n").split(' '))

#Setup finished


