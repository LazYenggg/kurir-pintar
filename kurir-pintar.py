import pygame
import random
from pygame.locals import *
from tkinter import filedialog, Tk
from PIL import Image
from collections import deque
import heapq
import time

#inisialisasi layar - Farrel
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600
JALAN_COLOR_RANGE = [(90, 90, 90), (150, 150, 150)]

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Smart Kurir")
font = pygame.font.SysFont(None, 30)

#variabel - Farrel
map_image = None
map_surface = None
kurir_pos = (0, 0)
kurir_dir = "RIGHT"
source_pos = (0, 0)
dest_pos = (0, 0)
highlight_path = []
info_lines = []

#fungsi - Farrel
def is_road(image, pos):
    x, y = pos
    if x < 0 or y < 0 or x >= image.width or y >= image.height:
        return False
    pixel = image.getpixel((x, y))
    return all(JALAN_COLOR_RANGE[0][i] <= pixel[i] <= JALAN_COLOR_RANGE[1][i] for i in range(3))

def random_road_position(image):
    while True:
        x = random.randint(0, image.width - 1)
        y = random.randint(0, image.height - 1)
        if is_road(image, (x, y)):
            return x, y

def update_direction(path, current_pos):
    global kurir_dir
    i = path.index(current_pos)
    if i + 1 < len(path):
        next_pos = path[i + 1]
        dx = next_pos[0] - current_pos[0]
        dy = next_pos[1] - current_pos[1]
        if dx == 1: kurir_dir = "RIGHT"
        elif dx == -1: kurir_dir = "LEFT"
        elif dy == -1: kurir_dir = "UP"
        elif dy == 1: kurir_dir = "DOWN"