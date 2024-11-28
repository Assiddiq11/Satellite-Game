import pzgrun
from random import randint
from time import time

WIDTH = 800
HEIGHT = 600

satellites = []
lines = []

next_satellite = 0
start_time = 0
total_time = 0
end_time = 0

number_of_satellites = 8

def draw_satellite():
    global start_time
    for count in range(0,number_of_satellites):
        satellite = Actor("satellite")
        satellite.pos = randint(40,WIDTH-40,) randint(40,HEIGHT-40)
        satellites.append(satellite)
    start_time = time()

def draw():
    global total_time
    screen.blit = ("background",(0,0))
    number = 1
    for satellite in satellites:


