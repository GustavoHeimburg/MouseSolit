import pyautogui as pg
import random
import time
from PIL import Image
import pygame
import pyautogui

pygame.mixer.init()
pygame.mixer.music.set_volume(0.2)

while True:
    x = random.randint(600, 1200)
    y = random.randint(100, 1200)

    for _ in range(5):
        r, g, b = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
        color = (r, g, b)
        pg.moveTo(x, y, 0.2)
        pg.click(button='left')
        pg.click(button='left')


        img = Image.new('RGB', (100, 100), color)
        img.show()
        time.sleep(0.1)

    rand_x, rand_y = random.randint(0, 1920), random.randint(0, 1080)
    screenshot = pyautogui.screenshot(region=(rand_x, rand_y, 100, 100))
    screenshot.show()

    pygame.mixer.music.play()
    time.sleep(5)

    time.sleep(random.random() * 3)
