from adafruit_circuitplayground import cp
import time
import random

MAX_PIXEL = 9
BLACK = (0, 0, 0)

# a function that returns a tuple with the red, green and blue values randomly generated.
def pixel_color():
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    return (red, green, blue)

# a function to turn all pixels off
def pixel_black():
    for i in range(MAX_PIXEL + 1):
        cp.pixels[i] = BLACK

# create empty lists
int_list = []
pattern = []

# open "pixel-pattern.txt" to read
with open ("pixel-pattern.txt", "r") as pattern_file:

    # reads string from file, splits at ", " and assigns it to "int_list"
    i_list = pattern_file.read()
    int_list = i_list.split(", ")

    # converts list of of string values into integers and appends them to "pattern"
    for string in int_list:
        i = int(string)
        pattern.append(i)

# inside the infinite while loop use a for loop to iterate through the pattern list
while True:
    for pixel in pattern:
        pixel_black()
        time.sleep(.1)
        cp.pixels[pixel] = pixel_color()
        time.sleep(.15)