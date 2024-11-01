import pygame as pg


class BaseElement():
    def __init__(self,
                 img: str,
                 start_position_x: int,
                 start_position_y: int,
                 step: int):
        self.img = pg.image.load(img)
        self.x = start_position_x
        self.y = start_position_y
        self.step = step
