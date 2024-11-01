import random

import pygame as pg

from players.player import Player
from players.enemy import Enemy
from players.rocket import Rocket
from const import (RES,
                   DISPLAY_WIDTH,
                   DISPLAY_HIGHT,
                   FPS,
                   BG_COLOR,
                   PLAYER_IMG,
                   ENEMY_IMG,
                   ROCKET_IMG,
                   IMG_SIZE,
                   STEP_PLAYER,
                   STEP_ENEMY)


def run():
    pg.init()
    screen = pg.display.set_mode(RES)

    # set caption
    pg.display.set_caption("SHOOTER")
    # set icon
    icon = pg.image.load(PLAYER_IMG)
    pg.display.set_icon(icon)

    # player
    player = Player(PLAYER_IMG,
                    DISPLAY_WIDTH // 2,
                    DISPLAY_HIGHT // 3 * 2,
                    STEP_PLAYER)
    # rocket
    rocket = Rocket(ROCKET_IMG,
                    None,
                    None,
                    STEP_ENEMY)
    # enemies
    enemies = []
    for i in range(DISPLAY_WIDTH // (IMG_SIZE * 2)):
        enemies.append(Enemy(ENEMY_IMG, IMG_SIZE * 2 * i, 0, STEP_ENEMY))

    clock = pg.time.Clock()
    is_players_shoot = False
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_LEFT or event.key == pg.K_a:
                    player.move_left()
                if event.key == pg.K_RIGHT or event.key == pg.K_d:
                    player.move_right()
                if event.key == pg.K_UP or event.key == pg.K_w:
                    player.move_up()
                if event.key == pg.K_DOWN or event.key == pg.K_s:
                    player.move_down()
                if event.key == pg.K_SPACE:
                    if is_players_shoot is False:
                        rocket.x = player.x
                        rocket.y = player.y - IMG_SIZE
                        is_players_shoot = True

        # set background color
        screen.fill(BG_COLOR)
        # update img
        screen.blit(player.img, (player.x, player.y))
        for enemy in enemies:
            if random.randint(0, 1):
                enemy.move_down()
            screen.blit(enemy.img, (enemy.x, enemy.y))
        if is_players_shoot:
            rocket.move_up()
            screen.blit(rocket.img, (rocket.x, rocket.y))
            if rocket.y == 0:
                is_players_shoot = False
        pg.display.update()
        clock.tick(FPS)


if __name__ == '__main__':
    run()
