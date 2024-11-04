import pygame as pg


class BaseElement():
    def __init__(self,
                 img: str,
                 step: int = 0,
                 start_position_x: int = None,
                 start_position_y: int = None,
                 health: int = 1):
        self.img = pg.image.load(img)
        self.x = start_position_x
        self.y = start_position_y
        self.step = step
        self.health = health
