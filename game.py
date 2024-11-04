import random

import pygame as pg

from players.player import Player
from players.enemy import Enemy
from players.rocket import Rocket
from players.base_element import BaseElement
from const import (RES,
                   DISPLAY_WIDTH,
                   DISPLAY_HIGHT,
                   FPS,
                   BG_COLOR,
                   PLAYER_IMG,
                   ENEMY_IMG,
                   ROCKET_IMG,
                   EXPLOSE_IMG,
                   WIN_IMG,
                   GAME_OVER_IMG,
                   IMG_SIZE,
                   STEP_PLAYER,
                   STEP_ENEMY)


class Game():
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode(RES)

        # set caption
        pg.display.set_caption("SHOOTER")
        # set icon
        pg.display.set_icon(pg.image.load(PLAYER_IMG))

        # player
        self.player = Player(PLAYER_IMG,
                             STEP_PLAYER,
                             DISPLAY_WIDTH // 2,
                             DISPLAY_HIGHT // 3 * 2)
        # rocket
        self.rocket = Rocket(ROCKET_IMG,
                             STEP_ENEMY)
        # explose
        self.explose = BaseElement(EXPLOSE_IMG, health=0)
        # message
        self.message = None
        # enemies
        self.enemies = []
        for i in range(DISPLAY_WIDTH // (IMG_SIZE * 2)):
            self.enemies.append(Enemy(
                ENEMY_IMG,
                STEP_ENEMY,
                IMG_SIZE * 2 * i,
                0)
            )

        self.clock = pg.time.Clock()
        self.is_players_shoot = False
        self.is_game_over = False

    def run(self):
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    return

                if self.is_game_over is False:
                    if event.type == pg.KEYDOWN:
                        if event.key == pg.K_LEFT or event.key == pg.K_a:
                            self.player.move_left()
                        if event.key == pg.K_RIGHT or event.key == pg.K_d:
                            self.player.move_right()
                        if event.key == pg.K_UP or event.key == pg.K_w:
                            self.player.move_up()
                        if event.key == pg.K_DOWN or event.key == pg.K_s:
                            self.player.move_down()
                        if event.key == pg.K_SPACE:
                            if self.is_players_shoot is False:
                                self.rocket.x = self.player.x
                                self.rocket.y = self.player.y - IMG_SIZE
                                self.is_players_shoot = True

            # set background color
            self.screen.fill(BG_COLOR)

            if self.is_game_over:
                self.message.health -= 1
                if self.message.health <= 0:
                    return
                self.screen.blit(
                    self.message.img,
                    (self.message.x, self.message.y)
                )
            else:
                # update player
                if self.player.health > 0:
                    self.screen.blit(
                        self.player.img,
                        (self.player.x, self.player.y)
                    )
                # update rocket
                if self.is_players_shoot:
                    self.rocket.move_up()
                    self.screen.blit(
                        self.rocket.img,
                        (self.rocket.x, self.rocket.y)
                    )
                    if self.rocket.y == 0:
                        self.is_players_shoot = False
                # update enemies
                index_enemy_to_remove = -1
                for i, enemy in enumerate(self.enemies):
                    if random.randint(0, 1):
                        enemy.move_down()
                    if self.is_players_shoot:
                        y_difference = abs(enemy.y - self.rocket.y)
                        if y_difference < IMG_SIZE and enemy.x == self.rocket.x:
                            index_enemy_to_remove = i
                            self.is_players_shoot = False
                            self.explose.x = enemy.x
                            self.explose.y = enemy.y
                            self.explose.health = FPS / 2
                    if index_enemy_to_remove != i:
                        y_difference = abs(enemy.y - self.player.y)
                        if y_difference < IMG_SIZE and enemy.x == self.player.x:
                            index_enemy_to_remove = i
                            self.player.health -= 1
                            self.explose.x = self.player.x
                            self.explose.y = self.player.y
                            self.explose.health = FPS / 2
                    if index_enemy_to_remove != i:
                        self.screen.blit(enemy.img, (enemy.x, enemy.y))
                if index_enemy_to_remove > -1:
                    del self.enemies[index_enemy_to_remove]
                if self.explose.health > 0:
                    self.explose.health -= 1
                    self.screen.blit(
                        self.explose.img,
                        (self.explose.x, self.explose.y)
                    )
                if self.player.health <= 0:
                    self.message = BaseElement(
                        GAME_OVER_IMG,
                        0,
                        DISPLAY_WIDTH // 2 - 75,
                        DISPLAY_HIGHT // 2 - 75,
                        FPS * 2
                    )
                    self.is_game_over = True
                elif len(self.enemies) == 0:
                    self.message = BaseElement(
                        WIN_IMG,
                        0,
                        DISPLAY_WIDTH // 2 - 75,
                        DISPLAY_HIGHT // 2 - 75,
                        FPS * 2
                    )
                    self.is_game_over = True
            pg.display.update()
            self.clock.tick(FPS)
