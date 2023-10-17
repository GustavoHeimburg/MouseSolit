import pyautogui as pg
import random
import time

while True:

    x = random.randint(600, 1200)
    y = random.randint(100,1200)
    pg.moveTo(x, y, 0.2)
    time.sleep(random.random() * 3)