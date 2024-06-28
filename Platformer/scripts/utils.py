import pygame as pg


BASE_IMG_PATH = "assets/images/"

def load_image(path):
    img = pg.image.load(BASE_IMG_PATH + path).convert()
    img.set_colorkey((0, 0, 0))

    return img