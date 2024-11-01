from players.base_element import BaseElement


class Rocket(BaseElement):
    def move_up(self):
        self.y -= self.step
        if self.y < 0:
            self.y = 0
