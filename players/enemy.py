from players.base_element import BaseElement
from const import DISPLAY_HIGHT, IMG_SIZE


class Enemy(BaseElement):
    def move_down(self):
        self.y += self.step
        if (self.y + IMG_SIZE) > DISPLAY_HIGHT:
            self.y = 0
