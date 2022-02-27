from PIL import Image
from numpy import asarray
import random
import time
import os

def translateimg(img:str):
    image = Image.open(img)
    data = asarray(image)

    map = {}
    for i in range(1, image.size[1] + 1):
        map[i] = []

    x, y = 0, 0

    for i in data:
        y += 1
        x = -1

        for j in i:
            x += 1
            current = str(j).replace(']', '').replace('[', '').replace('   ', ' ').replace('  ', ' ').replace('   ', ' ').split()
            current[0] = int(current[0])
            current[1] = int(current[1])
            current[2] = int(current[2])

            map[y].append([])
            map[y][x] = current
    
    return map

def render(map:dict):
    os.system('clear')
    for i in map.keys():
        final = ''
        for x in map[i]:
            rgb = x
            final += f'\033[38;2;{rgb[0]};{rgb[1]};{rgb[2]}m{random.choice([0, 1])}{random.choice([0, 1])}'
        print(final)

render(translateimg('scream.jpeg'))