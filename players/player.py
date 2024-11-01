from players.base_element import BaseElement
from const import DISPLAY_WIDTH, DISPLAY_HIGHT, IMG_SIZE


class Player(BaseElement):
    def move_left(self):
        self.x -= self.step
        if self.x < 0:
            self.x = 0

    def move_right(self):
        self.x += self.step
        if (self.x + IMG_SIZE) > DISPLAY_WIDTH:
            self.x = DISPLAY_WIDTH - IMG_SIZE

    def move_up(self):
        self.y -= self.step
        if self.y < 0:
            self.y = 0

    def move_down(self):
        self.y += self.step
        if (self.y + IMG_SIZE) > DISPLAY_HIGHT:
            self.y = DISPLAY_HIGHT - IMG_SIZE
