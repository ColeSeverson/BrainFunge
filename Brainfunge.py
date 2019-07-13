import fileinput
import sys

#ALL Setup

#Input and Memory
sourceInput = []
tape = [0] * 1024
#Constant Directions
RIGHT = (0, 1)
LEFT = (0, -1)
UP = (-1, 0)
DOWN = (1, 0)
MAXINT = sys.maxsize

direction = RIGHT
pos = (0, 0)
pointer = 0

for line in fileinput.input():
    sourceInput.append(line.rstrip("\r\n"))

while(True):
    if(pos[0] >= len(sourceInput) or pos[1] >= len(sourceInput[pos[0]])
            or pos[0] < 0 or pos[1] < 0 or pointer < 0 or pointer > 1023):
        break
    symbol = sourceInput[pos[0]][pos[1]]
    #tape options
    if symbol == '+':
        tape[pointer] += 1
    elif symbol == '-':
        tape[pointer] -= 1
    #pointer options
    elif symbol == '/':
        pointer += 1
    elif symbol == '\\':
        pointer -= 1
    #Directional options
    elif symbol == ">":
        direction = RIGHT
    elif symbol == "<":
        direction = LEFT
    elif symbol == "^":
        direction = UP
    elif symbol == "v":
        direction = DOWN
    #Print options
    elif symbol == 'c': #handling newline
        print(chr(tape[pointer]), end = "")
    elif symbol == 'i':
        print(int(tape[pointer]), end = "")
    #TODO add conditionals 
    elif symbol == '|':
        if tape[pointer] == 0:
            direction = UP
        else:
            direction = DOWN
    elif symbol == '-':
        if tape[pointer] == 0:
            direction == LEFT
        else:
            direction == DOWN
     
    pos = (pos[0] + direction[0], pos[1] + direction[1])
#Setup finished

