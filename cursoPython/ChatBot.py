#TODO CONHECIMENTO DO CURSO SERA ANOTADO EM PRATICA NAS CLASSES.

import time
import pyautogui

def check_for_new_messages():

    return True


def send_message(message):
    pyautogui.typewrite(message)
    pyautogui.press('enter')

while True:
    if check_for_new_messages():
        new_message = "Olá! Esta é uma resposta automática do chatbot."
        print(new_message)

    time.sleep(1)
