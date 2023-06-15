import numpy as np
from PIL import ImageGrab, ImageOps
import pyautogui as py
import time

# Una función para realizar un salto en el juego.
def salto():
    py.keyDown('space')
    time.sleep(0.1)
    py.keyUp('space')

# Calcula el área del escenario en el juego.
def calcularArea(Box):
    image = ImageGrab.grab(Box)
    image = ImageOps.grayscale(image)
    arr = np.array(image.getcolors())
    return arr.sum()

def run():
    while True:
        # Definir las coordenadas de las áreas en el juego
        box1 = (730, 200, 850, 222)
        box2 = (400, 200, 520, 222)

        # Calcular el área de cada región
        area1 = calcularArea(box1)
        area2 = calcularArea(box2)

        # Calcular la diferencia porcentual entre las áreas
        diferencia = abs(area2 - area1) / area1 * 100

        # Si la diferencia es mayor o igual a 2, realizar un salto
        if diferencia >= 2:
            salto()

run()